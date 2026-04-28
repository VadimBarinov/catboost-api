from catboost import CatBoostRegressor
from config import settings

class ModelLoader:
  def __init__(self):
    self.model = CatBoostRegressor()
    
  def load_model(self):
    self.model.load_model(settings.model_path)
    return self.model