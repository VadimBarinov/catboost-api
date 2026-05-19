from pydantic import BaseModel
from typing import List

class ActivityDto(BaseModel):
  id: int
  type: str
  distance: float
  moving_time: float 
  average_speed: float 
  total_elevation_gain: float 
  average_heartrate: float 
  intensity_score: float | None = None
  target: int | None = None
  
class ActivityListDto(BaseModel):
  content: List[ActivityDto]