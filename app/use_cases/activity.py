from .dtos import ActivityDto, ActivityListDto
from app.domain.predict import ScorePredicter

class IntesityScorePredicter:
  def __init__(self, score_predicter=ScorePredicter):
    self.score_predicter = score_predicter()
    
  def predict_score(self, activity: ActivityDto):
    score = self.score_predicter.predict_one(
      activity.model_dump(exclude={"intensity_score", "target"})
    )
    return score

class CogganZoneLabeler:
  def __init__(self):
    self.zone_boundaries = {
      1: 0.55, 2: 0.75, 3: 0.90,
      4: 1.05, 5: 1.20, 6: 1.50, 7: 1.51
    }

  def assign_zone(self, intensity_score):
    if intensity_score < self.zone_boundaries[1]: return 1
    elif intensity_score < self.zone_boundaries[2]: return 2
    elif intensity_score < self.zone_boundaries[3]: return 3
    elif intensity_score < self.zone_boundaries[4]: return 4
    elif intensity_score < self.zone_boundaries[5]: return 5
    elif intensity_score < self.zone_boundaries[6]: return 6
    else: return 7

class TargetCalculater:
  def __init__(self, 
               intensity_score_predicter=IntesityScorePredicter, 
               coggan_zone_labeler=CogganZoneLabeler):
    self.intensity_score_predicter = intensity_score_predicter()
    self.coggan_zone_labeler = coggan_zone_labeler()
  
  def calculate(self, activity_list: list):
    activity_list_dto = ActivityListDto(
      content=[
        ActivityDto(
          type=a.type,
          distance=a.distance,
          moving_time=a.moving_time, 
          average_speed=a.average_speed, 
          total_elevation_gain=a.total_elevation_gain, 
          average_heartrate=a.average_heartrate, 
        )
        for a in activity_list
      ]
    )
    for activity in activity_list_dto.content:
      activity.intensity_score = self.intensity_score_predicter.predict_score(activity)
      activity.target = self.coggan_zone_labeler.assign_zone(activity.intensity_score)
    return activity_list_dto