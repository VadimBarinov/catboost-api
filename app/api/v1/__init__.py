from flask_openapi3 import APIBlueprint
from .tags import v1_tag
from config import settings

bp = APIBlueprint("v1", __name__, abp_tags=[v1_tag,],
                      url_prefix=settings.routes.v1)   

from . import routes
