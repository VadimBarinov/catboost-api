from http import HTTPStatus
from app.schemas.activity import ActivityRequest, ActivityResponse
from . import bp

@bp.post("/", summary="Получить тип тренировки",
        responses={HTTPStatus.OK: ActivityResponse})
def get_all_users(body: ActivityRequest):
    response = 123
    return response, HTTPStatus.OK
