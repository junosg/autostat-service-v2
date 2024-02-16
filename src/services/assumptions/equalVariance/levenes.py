from scipy import stats

from src.services.statisticsTest import StatisticsTest
from src.services.assumptions.equalVariance.result import EqualVarianceResult

class LevenesTestResult:
    test: str
    areVariancesEqual: bool
    statistic: float
    pvalue: float
    passed: bool

class LevenesTest(StatisticsTest):
    name = "Levene's Test"

    def execute(self):
        result: EqualVarianceResult = EqualVarianceResult()
        
        result.test = self.name
        result.passed = True
        
        levenes = stats.levene(*self.testData.valueList, center = "mean")
        
        result.passed = bool(levenes.pvalue > 0.05)
        result.statistic = levenes.statistic
        result.pvalue = levenes.pvalue

        if result.passed:
            result.conclusion = f"The Levene's test results show a p-value of {result.pvalue}, indicating no significant difference in variances among {self.testData.predictor} groups. This means that the assumption of equal variances across groups is not violated."
        else:
            result.conclusion = f"The Levene's test results show a p-value of {result.pvalue}, indicating a significant difference in variances among {self.testData.predictor} groups. This means that the assumption of equal variances across groups is violated."

        return result