import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class _Configs(BaseModel):
    LOCAL_TZ: str = os.getenv('LOCAL_TZ')
    LOCAL_LANG: str = os.getenv('LOCAL_LANG')

    PROJECT_KEY: str = os.getenv('PROJECT_KEY')
    BACKEND_HOST: str = os.getenv('BACKEND_HOST')
    BACKEND_PORT: str = os.getenv('BACKEND_PORT')

    FRONTEND_HOST: str = os.getenv('FRONTEND_HOST')
    FRONTEND_PORT: str = os.getenv('FRONTEND_PORT')

    ROOT: str = os.getenv('ROOT')
    PASSWORD: str = os.getenv('PASSWORD')

    POSTGRESQL_HOST: str = os.getenv('POSTGRESQL_HOST')
    POSTGRESQL_PORT: str = os.getenv('POSTGRESQL_PORT')
    POSTGRESQL_USERNAME: str = os.getenv('POSTGRESQL_USERNAME')
    POSTGRESQL_PASSWORD: str = os.getenv('POSTGRESQL_PASSWORD')
    POSTGRESQL_DATABASE: str = os.getenv('POSTGRESQL_DATABASE')