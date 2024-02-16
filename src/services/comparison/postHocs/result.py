from src.models.comparisonTestData import ComparisonTestData
from src.services.comparison.result import ComparisonTestResult

class PostHocsComparisonTestResult(ComparisonTestResult):
    def setConclusion(self, testData: ComparisonTestData, leftGroup: str, rightGroup: str):
        if self.pvalue > testData.levelOfSignificance:
            self.conclusion = f"The result indicates a p-value of {self.pvalue}. Since this value is above the significant threshold of {testData.levelOfSignificance}, we can conclude that there is no significant difference in {testData.outcome} between {leftGroup} and {rightGroup} groups."
        else:
            self.conclusion = f"The result indicates a p-value of {self.pvalue}. Since this value is below the significant threshold of {testData.levelOfSignificance}, we can conclude that there is a significant difference in {testData.outcome} between {leftGroup} and {rightGroup} groups."