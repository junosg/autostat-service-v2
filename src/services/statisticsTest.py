from abc import abstractmethod
from ..models.testData import TestData

class StatisticsTest():
    name: str = "test"
    assumptionsPassed: bool = True
    assumptionsResults: dict = {}
    assumptionsConclusion: str
    
    testData: TestData
    
    def __init__(self, testData: TestData) -> None:
        self.testData = testData

    @abstractmethod
    def checkAssumptions(self):
        pass
    
    @abstractmethod
    def execute(self):
        pass