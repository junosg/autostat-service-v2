from pydantic import BaseModel

class PerformTestRequest(BaseModel):
    data: list
    levelOfSignificance: float
    predictor: str
    outcome: str
    predictorPaired: bool
