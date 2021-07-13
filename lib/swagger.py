from marshmallow import fields, Schema
from sanic_openapi.openapi3 import openapi

MAP_MARSHMALLOW_IN_OPEN_API = {
    fields.DateTime: openapi.DateTime,
    fields.Date: openapi.Date,
    fields.Integer: openapi.Integer,
    fields.String: openapi.String,
    fields.Boolean: openapi.Boolean,
    fields.List: openapi.Array
}


def open_api_schemas(schemas: Schema):
    """
    Отдает схему для swagger документации получая из marshmallow схему
    """
    swagger_schema = {}
    for field_key in schemas.fields:
        field_obj = schemas.fields[field_key]
        swagger_schema[field_key] = marshmallow_to_swagger(field_key, field_obj)
    return swagger_schema


def open_api_schemas_params(schemas: Schema):
    """
    Отдает схему для swagger документации получая из marshmallow схему
    Для Query-параметров
    """
    params = []
    for field_key in schemas.fields:
        field_obj = schemas.fields[field_key]
        params.append(marshmallow_to_swagger(field_key, field_obj))

    return params


def marshmallow_to_swagger(field_key, field_obj):
    field_type = type(field_obj)
    if isinstance(field_obj, fields.Nested):
        return open_api_schemas(field_obj.schema)
    else:
        doc_type = MAP_MARSHMALLOW_IN_OPEN_API.get(field_type, openapi.String)
        required = getattr(field_obj, 'required', False)
        swagger_type = doc_type(name=field_key, required=required)
        if doc_type == openapi.Array:
            sub_type = type(field_obj.container)
            sub_type = marshmallow_to_swagger(field_obj.container.name, sub_type)
            swagger_type.items = [sub_type]
        return swagger_type