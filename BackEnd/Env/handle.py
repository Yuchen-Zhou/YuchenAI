import os
from dotenv import load_dotenv

load_dotenv()


class Configs:
    LOCAL_TZ = os.getenv('LOCAL_TZ')
    LOCAL_LANG = os.getenv('LOCAL_LANG')

    PROJECT_KEY = os.getenv('PROJECT_KEY')
    BACKEND_HOST = os.getenv('BACKEND_HOST')  # 注意这里的拼写错误
    BACKEND_PORT = os.getenv('BACKEND_PORT')

    FRONTEND_HOST = os.getenv('FRONTEND_HOST')
    FRONTEND_PORT = os.getenv('FRONTEND_PORT')

    ROOT = os.getenv('ROOT')
    PASSWORD = os.getenv('PASSWORD')

    POSTGRESQL_HOST = os.getenv('POSTGRESQL_HOST')
    POSTGRESQL_PORT = os.getenv('POSTGRESQL_PORT')
    POSTGRESQL_USERNAME = os.getenv('POSTGRESQL_USERNAME')
    POSTGRESQL_PASSWORD = os.getenv('POSTGRESQL_PASSWORD')
    POSTGRESQL_DATABASE = os.getenv('POSTGRESQL_DATABASE')

    @classmethod
    def get_local_tz(cls):
        return cls.LOCAL_TZ

    @classmethod
    def get_local_lang(cls):
        return cls.LOCAL_LANG

    @classmethod
    def get_project_key(cls):
        return cls.PROJECT_KEY

    @classmethod
    def get_backend(cls):
        return cls.BACKEND_HOST + ":" + cls.BACKEND_PORT

    @classmethod
    def get_frontend(cls):
        return cls.FRONTEND_HOST + ":" + cls.FRONTEND_PORT

    @classmethod
    def get_postgresql(cls):
        return cls.POSTGRESQL_HOST + ":" + cls.POSTGRESQL_PORT

    @classmethod
    def get_postgresql_username(cls):
        return cls.POSTGRESQL_USERNAME

    @classmethod
    def get_postgresql_password(cls):
        return cls.POSTGRESQL_PASSWORD

    @classmethod
    def get_postgresql_database(cls):
        return cls.POSTGRESQL_DATABASE


    @classmethod
    def get_params(cls):
        return {
            'LOCAL_TZ': cls.LOCAL_TZ,
            'LOCAL_LANG': cls.LOCAL_LANG,
            'PROJECT_KEY': cls.PROJECT_KEY,
            'BACKEND_HOST': cls.BACKEND_HOST,
            'BACKEND_PORT': cls.BACKEND_PORT,
            'FRONTEND_HOST': cls.FRONTEND_HOST,
            'FRONTEND_PORT': cls.FRONTEND_PORT,
            'ROOT': cls.ROOT,
            'PASSWORD': cls.PASSWORD,
            'POSTGRESQL_HOST': cls.POSTGRESQL_HOST,
            'POSTGRESQL_PORT': cls.POSTGRESQL_PORT,
            'POSTGRESQL_USERNAME': cls.POSTGRESQL_USERNAME,
            'POSTGRESQL_PASSWORD': cls.POSTGRESQL_PASSWORD,
            'POSTGRESQL_DATABASE': cls.POSTGRESQL_DATABASE,
        }


configs = Configs()