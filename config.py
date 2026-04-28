from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
    )
from pydantic import BaseModel
from pathlib import Path
import os

BASE_DIR = Path(__file__).parent.parent.parent

APP_ENV = os.getenv("APP_ENV", "development")

ENV_FILES = {
    "development": ".env",
    "test":        ".env.test",
    "staging":     ".env.staging",
    "production":  ".env.production",
}

env_file = ENV_FILES.get(APP_ENV, ".env")

class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 5000
    
class RoutesConfig(BaseModel):
    vadim_onboarding: str = "/vadim-onboarding"
    vadim_onboarding_tag: str = "Vadim Onboarding"
    
    doc_prefix: str = vadim_onboarding + "/docs"
    doc_url: str = vadim_onboarding + "/docs.json"
    
    home: str = ""
    home_tag: str = "Home"
    home_description: str = "Домашняя страница"
    
    health_check: str = "/health-check"
    health_check_tag: str = "Health Check"
    health_check_description: str = "Проверка работоспособности"
    
    users: str = "/users"
    users_tag: str = "Users"
    users_description: str = "Операции с пользователями"
    
class ErrorsConfig(BaseModel):
    NOT_FOUND_USER: str = "Пользователь не найден"
    DUPLICATE_USER: str = "Пользователь с таким username или email уже существует"
    BAD_REQUEST: str = "Неверный запрос"

class Settings(BaseSettings):
    database_url: str
    app_env: str
    flask_app: str
    run: RunConfig = RunConfig()
    routes: RoutesConfig = RoutesConfig()
    errors: ErrorsConfig = ErrorsConfig()
    model_config = SettingsConfigDict(
        env_file=(BASE_DIR / env_file),
        case_sensitive=False,
    )

settings = Settings()