from app.app import app
from sanic.log import logger
from settings import APP_HOST, APP_PORT, DEBUG


def run():
    try:
        app.go_fast(host=APP_HOST, port=APP_PORT, debug=DEBUG)
    except Exception as ex:
        logger.exception("stop_app ex=%s", ex)
        raise
