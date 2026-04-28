import pandas as pd
from .model import ModelLoader

class ScorePredicter:
  def __init__(self, model=ModelLoader):
    self.model = model().load_model()
  
  def predict_one(self, features: dict) -> float:
    df = pd.DataFrame([features])
    pred = self.model.predict(df)
    return float(pred[0])