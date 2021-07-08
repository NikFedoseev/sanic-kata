from aiopg.sa import Engine
from sanic import Sanic
from sanic.request import Request


class CustomCtx():
    db_engine: Engine


class AppSanic(Sanic):
    ctx: CustomCtx


class AppRequest(Request):
    app: AppSanic