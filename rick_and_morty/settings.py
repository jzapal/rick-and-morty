import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PORT: int = 8000
    API_HOST: str = '0.0.0.0'
    PAGE_SIZE: int = 10

    @property
    def root_dir(self):
        return os.path.dirname(os.path.realpath(__file__))


settings = Settings()
