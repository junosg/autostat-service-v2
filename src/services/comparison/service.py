from src.models.comparisonTestData import ComparisonTestData

from src.services.comparison.twoGroups.service import TwoGroupsService
from src.services.comparison.pairedGroups.service import PairedGroupsService
from src.services.comparison.manyGroups.service import ManyGroupsService

class ComparisonService():
    twoGroupsService: TwoGroupsService
    pairedGroupsService: PairedGroupsService
    manyGroupsService: ManyGroupsService
    
    testData: ComparisonTestData
    
    def __init__(self, testData: ComparisonTestData) -> None:
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