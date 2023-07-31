"""Config module."""

from pydantic import BaseSettings


class Config(BaseSettings):
    title: str
    app_port: int = 8001


config = Config()
