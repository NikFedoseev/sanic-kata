from sanic import Blueprint, HTTPMethod

from handler.api.v1 import student

api = Blueprint('api', url_prefix='/api/v1')
api.add_route(student.get_students, '/students', methods=(HTTPMethod.GET, ))
api.add_route(student.create_student, '/students', methods=(HTTPMethod.POST, ))
api.add_route(student.get_student_by_id, '/students/<id>', methods=(HTTPMethod.GET, ))
api.add_route(student.update_student_by_id, '/students/<id>', methods=(HTTPMethod.PATCH, ))
api.add_route(student.delete_student_by_id, '/students/<id>', methods=(HTTPMethod.DELETE, ))
