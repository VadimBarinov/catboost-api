from flask_openapi3 import OpenAPI, Info
from config import settings

def create_app() -> OpenAPI:
  info = Info(title="CatBoost Сategorization Coggan Zone", version="1.0.0")
  app = OpenAPI(
    __name__,
    info=info,
    doc_prefix=settings.routes.doc_prefix,
    doc_url=settings.routes.doc_url,
  )

  from .api import bp as api_bp
  app.register_api(api_bp)
      
  return app