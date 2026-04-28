from flask_openapi3 import APIBlueprint
from .tags import api_tag
from config import settings

bp = APIBlueprint("api", __name__, abp_tags=[api_tag,],
                      url_prefix=settings.routes.api)

from .v1 import bp as v1_bp
bp.register_api(v1_bp)
