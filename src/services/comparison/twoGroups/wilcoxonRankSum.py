from scipy import stats

from src.services.comparison.statisticsTest import ComparisonStatisticsTest
from src.services.comparison.result import ComparisonTestResult

class WilcoxonRankSumTest(ComparisonStatisticsTest):
    name = "Wilcoxon Rank-Sum Test"
    
    def checkAssumptions(self):
        self.assumptionsConclusion = f"Since the assumptions of normality and equal variances are not required for the {self.name}, we can confidently utilize this test to compare the distributions of {self.testData.outcome} between {self.testData.predictor} groups"
          
    
    def execute(self):
        result = stats.ranksums(*self.testData.valueList)

        returnValue = ComparisonTestResult()
        returnValue.test = self.name
        returnValue.statistic = result.statistic
        returnValue.pvalue = result.pvalue

        returnValue.setConclusion(self.testData)

        return returnValue