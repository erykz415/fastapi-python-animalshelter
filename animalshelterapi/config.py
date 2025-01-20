"""A module providing configuration variables."""

from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    """A class containing base settings configuration."""
    model_config = SettingsConfigDict(extra="ignore")


class AppConfig(BaseConfig):
    """A class containing app's configuration."""
    DB_HOST: Optional[str] = "localhost"
    DB_NAME: Optional[str] = "animalshelter"
    DB_USER: Optional[str] = "postgres"
    DB_PASSWORD: Optional[str] = "passx"


config = AppConfig()
