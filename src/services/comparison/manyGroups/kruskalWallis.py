from scipy import stats

from src.services.comparison.statisticsTest import ComparisonStatisticsTest
from src.services.comparison.result import ComparisonTestResult

class KruskalWallisTest(ComparisonStatisticsTest):
    name = "Kruskal-Wallis H Test"

    def checkAssumptions(self):
        self.assumptionsConclusion = f"Since the assumptions of normality and equal variances are not required for the {self.name}, we can confidently utilize this test to compare the distributions of {self.testData.outcome} between {self.testData.predictor} groups"
    
    def execute(self):
        result = stats.kruskal(*self.testData.valueList)
        
        returnValue = ComparisonTestResult()
        returnValue.test = self.name
        returnValue.statistic = result.statistic
        returnValue.pvalue = result.pvalue
       
        if result.pvalue > self.testData.levelOfSignificance:
            returnValue.conclusion = f"The {self.name} results indicate a p-value of {result.pvalue}. Since this value is above the significant threshold of {self.testData.levelOfSignificance}, we can conclude that there is no significant difference in {self.testData.outcome} between {self.testData.predictor} groups."
        else:
            returnValue.conclusion = f"The {self.name} results indicate a p-value of {result.pvalue}. Since this value is below the significant threshold of {self.testData.levelOfSignificance}, we can conclude that there is a significant difference in {self.testData.outcome} between {self.testData.predictor} groups."

        # if (result.pvalue < 0.05):
        #     returnValue["postHoc"] = DunnsTest(self.dataSource).execute()

        return returnValue