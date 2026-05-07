from http import HTTPStatus
from app.schemas.activity import ActivityListRequest, ActivityListResponse, ActivityResponse
from app.use_cases.activity import TargetCalculater
from . import bp

@bp.post("/predict-type", summary="Получить тип тренировки",
        responses={HTTPStatus.OK: ActivityListResponse})
def calculate_intensity_score_and_target(body: ActivityListRequest):
  activity_list_with_calculated_target = TargetCalculater().calculate(body.content)
  response = ActivityListResponse(
    content=[
      ActivityResponse(
        type=a.type,
        distance=a.distance,
        moving_time=a.moving_time, 
        average_speed=a.average_speed, 
        total_elevation_gain=a.total_elevation_gain, 
        average_heartrate=a.average_heartrate, 
        intensity_score=a.intensity_score, 
        target=a.target, 
      )
      for a in activity_list_with_calculated_target.content
    ]
  )
  return response.model_dump(), HTTPStatus.OK
