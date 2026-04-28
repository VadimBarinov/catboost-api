from flask_openapi3 import Tag
from config import settings

api_tag = Tag(
  name=settings.routes.api_tag,
  description=settings.routes.api_description,
)
