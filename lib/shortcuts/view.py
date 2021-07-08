from sanic import response
from sanic.log import logger

from lib.utils import custom_dumps


def _error_http_response(msg: str, code: int, headers=None):
    resp = response.json({
        'success': False,
        'errors': [{
            'code': code,
            'message': msg
        }] if isinstance(msg, str) else msg
    }, status=code, dumps=custom_dumps)

    if headers:
        resp.headers.update(headers)

    return resp


def _http_response(data: object, code: int, headers=None):
    resp = response.json({'success': True, 'result': data}, status=code, dumps=custom_dumps)
    if headers:
        resp.headers.update(headers)

    return resp


def http_ok(msg='OK', headers=None):
    code = 200

    return _http_response(msg, code, headers)


def http_created(msg='Created', headers=None):
    code = 201
    return _http_response(msg, code, headers)


def http_bad_request(msg='Bad request', headers=None):
    code = 400
    return _error_http_response(msg, code, headers=headers)


def http_not_found(msg='Not found', headers=None):
    code = 404
    return _error_http_response(msg, code, headers=headers)