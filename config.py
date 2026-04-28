from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).parent
    
class RoutesConfig(BaseModel):
  doc_prefix: str = "/docs"
  doc_url: str = "/docs.json"
  
  api: str = "/api"
  api_tag: str = "API"
  api_description: str = "Категоризация тренировок"
  
  v1: str = "/v1"
  v1_tag: str = "v1"
  v1_description: str = "v1"

class Settings(BaseSettings):
  flask_app: str
  routes: RoutesConfig = RoutesConfig()
  model_config = SettingsConfigDict(
    env_file=(BASE_DIR / ".env"),
    case_sensitive=False,
  )

settings = Settings()