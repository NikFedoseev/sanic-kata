import sqlalchemy as sa
from datetime import datetime
from models.student import Student
from core.core_app import AppRequest
from lib.shortcuts.view import http_ok, http_not_found, http_bad_request
from schemas.student import CreateStudentSchema, StudentSchema, UpdateStudetSchema
from marshmallow import ValidationError


async def create_student(request: AppRequest):
    async with request.app.ctx.db_engine.acquire() as conn:
        try:
            create_dto = CreateStudentSchema().load(request.json)
            stmt = sa.insert(Student).values(**create_dto).returning(Student.__table__)
            cur = await conn.execute(stmt)
            res = await cur.first()
            response = StudentSchema().dump(res)
            return http_ok(response)
        except ValidationError as err:
            return http_bad_request(err.messages)


async def get_students(request: AppRequest):
    async with request.app.ctx.db_engine.acquire() as conn:
        stmt = sa.select([Student])
        cur = await conn.execute(stmt)
        res = await cur.fetchall()
        response = StudentSchema().dump(res, many=True)
        return http_ok(response)


async def get_student_by_id(request: AppRequest, id: int):
    async with request.app.ctx.db_engine.acquire() as conn:
        stmt = sa.select([Student]).where(Student.id == id)
        cur = await conn.execute(stmt)
        res = await cur.first()
        if not res:
            return http_not_found('not found')
        response = StudentSchema().dump(res)
        return http_ok(response)


async def update_student_by_id(request: AppRequest, id: int):
    async with request.app.ctx.db_engine.acquire() as conn:
        try:
            update_dto = UpdateStudetSchema().load(request.json)
            stmt = sa.update(Student).where(Student.id == id).values(updated_at=datetime.utcnow(),
                                                                     **update_dto).returning(Student.__table__)
            cur = await conn.execute(stmt)
            res = await cur.first()
            if not res:
                return http_not_found('not found')
            response = StudentSchema().dump(res)
            return http_ok(response)
        except ValidationError as err:
            return http_bad_request(err.messages)


async def delete_student_by_id(request: AppRequest, id: int):
    async with request.app.ctx.db_engine.acquire() as conn:
        try:
            stmt = sa.delete(Student).where(Student.id == id).returning(Student.__table__)
            cur = await conn.execute(stmt)
            res = await cur.first()
            if not res:
                return http_not_found('not found')
            response = StudentSchema().dump(res)
            return http_ok(response)
        except BaseException:
            return http_bad_request('¯\_(ツ)_/¯')