from src.models.testData import TestData

from src.services.comparison.twoGroups.twoGroupsService import TwoGroupsService
from src.services.comparison.pairedGroups.pairedGroupsService import PairedGroupsService
from src.services.comparison.manyGroups.manyGroupsService import ManyGroupsService

class ComparisonService():
    twoGroupsService: TwoGroupsService
    pairedGroupsService: PairedGroupsService
    manyGroupsService: ManyGroupsService
    
    testData: TestData
    
    def __init__(self, testData: TestData) -> None:
        self.testData = testData

        self.twoGroupsService = TwoGroupsService(testData)
        self.pairedGroupsService = PairedGroupsService(testData)
        self.manyGroupsService = ManyGroupsService(testData)
        
    def analyze(self):
        result = {}

        if self.twoGroupsService.prereqPassed:
            result = self.twoGroupsService.analyze()
        elif self.pairedGroupsService.prereqPassed:
            result = self.pairedGroupsService.analyze()
        elif self.manyGroupsService.prereqPassed:
            result = self.manyGroupsService.analyze()

        return result