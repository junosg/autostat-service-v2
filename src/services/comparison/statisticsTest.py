from abc import abstractmethod
from ...models.comparisonTestData import ComparisonTestData

class ComparisonStatisticsTest():
    name: str = "test"
    assumptionsPassed: bool = True
    assumptionsResults: dict = {}
    assumptionsConclusion: str
    
    testData: ComparisonTestData
    
    def __init__(self, testData: ComparisonTestData) -> None:
        self.testData = testData

    @abstractmethod
    def checkAssumptions(self):
        pass
    
    @abstractmethod
    def execute(self):
        pass