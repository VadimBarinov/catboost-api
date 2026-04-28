from pydantic import BaseModel, Field
from typing import List

class ActivityRequest(BaseModel):
  type: str = Field(
    default=...,
    description="Тип тренировки (Ride/Run)",
  )
  distance: float = Field(
    default=...,
    description="Пройденное расстояние",
  )
  moving_time: float = Field(
    default=...,
    description="Время в движении",
  )
  average_speed: float = Field(
    default=...,
    description="Средняя скорость",
  )
  total_elevation_gain: float = Field(
    default=...,
    description="Общий набор высоты",
  )
  average_heartrate: float = Field(
    default=...,
    description="Средний пульс",
  )
  
class ActivityResponse(ActivityRequest):
  intensity_score: float = Field(
    default=...,
    description="Оценка интенсивности",
  )
  target: int = Field(
    default=...,
    description="Зона мощности",
  )
  
class ActivityListRequest(BaseModel):
  content: List[ActivityRequest]
  
class ActivityListResponse(BaseModel):
  content: List[ActivityResponse]