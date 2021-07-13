import os

from envparse import Env

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

env = Env()
env_file_path = os.path.join(BASE_DIR, '.env')
env.read_envfile(env_file_path)

APP_NAME = 'app_name'
APP_HOST = env.str('APP_HOST', default='localhost')
APP_PORT = env.int('APP_PORT', default=9090)

WORKERS = env.int('WORKERS', default=1)

ENV = env.str('ENV', default='local')
DEBUG = env.bool('DEBUG', default=False)
AUTO_RELOAD = env.bool('AUTO_RELOAD', default=False)

DB_HOST = env.str('DB_HOST', default='localhost')
DB_PORT = env.int('DB_PORT', default=5432)
DB_NAME = env.str('DB_NAME', default='appdb')
DB_USER = env.str('DB_USER', default='dbuser')
DB_PASSWORD = env.str('DB_PASSWORD', default='dbpass')
DB_MAX_CONNECTIONS = env.int('DB_MAX_CONNECTIONS', default=10)
DC_POOL_RECYCLE = env.int('DC_POOL_RECYCLE', default=60)

TEST_DB_HOST = env.str('DB_HOST', default='localhost')
TEST_DB_PORT = env.int('DB_PORT', default=5431)
TEST_DB_NAME = env.str('DB_NAME', default='appdb_test')
TEST_DB_USER = env.str('DB_USER', default='dbuser_test')
TEST_DB_PASSWORD = env.str('DB_PASSWORD', default='dbpass_test')
