import pytest
import settings

# Тут конфликт зависмостей Sanc 21.6 и pytest-sanic
# Sanic требует websocket >=9, pytest-sanic 8.1
# поэтому тесты пока не работаеют, до тех пор пока pytest-sanic не перейдет на новую версию websocket
# https://github.com/yunstanford/pytest-sanic/issues/55


@pytest.fixture(scope="session", autouse=True)
def sqlengine(request):
    from sqlalchemy import create_engine
    from models import Base

    test_db_url = f'postgresql://{settings.TEST_DB_USER}:{settings.TEST_DB_PASSWORD}@{settings.TEST_DB_HOST}:{settings.TEST_DB_PORT}/{settings.TEST_DB_NAME}'
    # почему не работает с aiopg.sa??
    engine = create_engine(test_db_url)
    Base.metadata.create_all(engine)

    yield engine
    Base.metadata.drop_all(sqlengine)


@pytest.fixture
def app():
    from app.app import app
    from core.core_app import AppSanic
    from aiopg.sa import create_engine

    @app.before_server_start
    async def setup_connect(app: AppSanic, loop):
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
    async def close_connect(app: AppSanic, loop):
        app.ctx.db_engine.close()
        await app.ctx.db_engine.wait_closed()

    yield app
