from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
    )
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8080
    
class RoutesConfig(BaseModel):
    doc_prefix: str = "/docs"
    doc_url: str = "/docs.json"
    
    home: str = ""
    home_tag: str = "Home"
    home_description: str = "Домашняя страница"

class Settings(BaseSettings):
    app_env: str
    flask_app: str
    run: RunConfig = RunConfig()
    routes: RoutesConfig = RoutesConfig()
    model_config = SettingsConfigDict(
        env_file=(BASE_DIR / ".env"),
        case_sensitive=False,
    )

settings = Settings()