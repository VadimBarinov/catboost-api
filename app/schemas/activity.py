from pydantic import BaseModel, Field

class ActivityRequest(BaseModel):
  type: str = Field(
    default=...,
    description="Тип тренировки (Ride/Run)",
  )
  distance: float = Field(
    default=...,
    description="Пройденное расстояние"
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
  pass