from flask_openapi3 import Tag
from config import settings

v1_tag = Tag(
  name=settings.routes.v1_tag,
)
