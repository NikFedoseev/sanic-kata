from marshmallow import Schema, fields
from datetime import datetime

from marshmallow.utils import EXCLUDE


class CreateStudentSchema(Schema):
    name = fields.String(required=True, error_messages={'required': 'Name is required'})

    class Meta:
        unknown = EXCLUDE


class UpdateStudetSchema(Schema):
    name = fields.String(required=False)
    active = fields.Boolean(required=False)

    class Meta:
        unknown = EXCLUDE


class StudentSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    active = fields.Boolean(required=True)
    created_at = fields.DateTime(format='%Y-%m-%dT%H:%M:%S+00:00', required=True)
    updated_at = fields.DateTime(format='%Y-%m-%dT%H:%M:%S+00:00', required=True)
