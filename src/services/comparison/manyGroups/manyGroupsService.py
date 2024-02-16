from src.models.testData import TestData
from src.services.statisticsTest import StatisticsTest
from src.services.comparison.result import ComparisonTestResult

from src.services.comparison.manyGroups.anova import AnovaTest
from src.services.comparison.manyGroups.kruskalWallis import KruskalWallisTest

class ManyGroupsService():
    tests: list[StatisticsTest] = [AnovaTest, KruskalWallisTest]
    
    def __init__(self, testData: TestData) -> None:
        self.checkPrerequisites(testData=testData)
        
        self.tests: list[StatisticsTest] = list(map(lambda test: test(testData), self.tests))

        for test in self.tests:
            test.checkAssumptions()
            
    def checkPrerequisites(self, testData: TestData):
        self.prereqPassed = bool(len(testData.columns) > 2)
        
    def analyze(self):
        returnValue = ComparisonTestResult()
        assumptionsResults = {}
        assumptionsConclusion = {}
        
        for index, test in enumerate(self.tests):
            if index == 0:
                assumptionsResults = test.assumptionsResults

            assumptionsConclusion[test.name] = test.assumptionsConclusion

            if test.assumptionsPassed:
                returnValue = test.execute()
                break
        
        returnValue.assumptions = {
                "result": assumptionsResults,
                "conclusion": assumptionsConclusion
            }

        return returnValue