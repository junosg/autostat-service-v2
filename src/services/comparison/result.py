from src.models.comparisonTestData import ComparisonTestData

class ComparisonTestResult():
    test: str
    statistic: float
    pvalue: float
    conclusion: str
    assumptions: dict
    postHoc: dict
    
    def setConclusion(self, testData: ComparisonTestData):
        if self.pvalue > testData.levelOfSignificance:
            self.conclusion = f"The {self.test} results indicate a p-value of {self.pvalue}. Since this value is above the significant threshold of {testData.levelOfSignificance}, we can conclude that there is no significant difference in {testData.outcome} between {testData.predictor} groups."
        else:
            self.conclusion = f"The {self.test} results indicate a p-value of {self.pvalue}. Since this value is below the significant threshold of {testData.levelOfSignificance}, we can conclude that there is a significant difference in {testData.outcome} between {testData.predictor} groups."