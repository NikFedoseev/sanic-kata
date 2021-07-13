from aiopg.sa import create_engine
from core.core_app import AppSanic
from core.logger_config import LOG_SETTINGS
from sanic_openapi import openapi3_blueprint
from routes import api
from settings import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME, DB_MAX_CONNECTIONS, DC_POOL_RECYCLE, APP_NAME, DEBUG


def set_router(app: AppSanic):
    app.blueprint(openapi3_blueprint)
    app.blueprint(api)


app = AppSanic(__name__, log_config=LOG_SETTINGS, strict_slashes=True)

set_router(app)


@app.before_server_start
async def setup_connect(app: AppSanic, _):
    app.ctx.db_engine = await create_engine(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        maxsize=DB_MAX_CONNECTIONS,
        application_name=APP_NAME,
        pool_recycle=DC_POOL_RECYCLE,
    )


@app.before_server_stop
async def close_connect(app: AppSanic, _):
    app.ctx.db_engine.close()
    await app.ctx.db_engine.wait_closed()
