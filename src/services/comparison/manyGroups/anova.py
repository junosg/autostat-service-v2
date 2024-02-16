from scipy import stats

from src.services.comparison.statisticsTest import ComparisonStatisticsTest
from src.services.comparison.result import ComparisonTestResult

from src.services.assumptions.normality.shapiroWilk import ShapiroWilkTest
from src.services.assumptions.equalVariance.levenes import LevenesTest
from src.services.comparison.postHocs.tukeys import TukeysTest

class AnovaTest(ComparisonStatisticsTest):
    name = "ANOVA Test"

    def checkAssumptions(self):
        normalityResult = ShapiroWilkTest(self.testData).execute()
        equalVarianceResult = LevenesTest(self.testData).execute()
        
        self.assumptionsPassed = bool(normalityResult.passed and equalVarianceResult.passed)
        self.assumptionsResults["normality"] = normalityResult
        self.assumptionsResults["equalVariance"] = equalVarianceResult
        
        if self.assumptionsPassed:
            self.assumptionsConclusion = f"Since the assumptions of normality and equal variances are not violated, we can confidently utilize {self.name} to compare the distributions of {self.testData.outcome} between {self.testData.predictor} groups."
        elif normalityResult.passed and equalVarianceResult.passed == False:
            self.assumptionsConclusion = f"Since the assumption of equal variances is violated, we cannot confidently utilize {self.name} to compare the distributions of {self.testData.outcome} between {self.testData.predictor} groups."
        elif equalVarianceResult.passed and normalityResult.passed == False:
            self.assumptionsConclusion = f"Since the assumption of normality is violated, we cannot confidently utilize {self.name} to compare the distributions of {self.testData.outcome} between {self.testData.predictor} groups."
        else:
            self.assumptionsConclusion = f"Since the assumptions of normality and equal variances are violated, we cannot confidently utilize {self.name} to compare the distributions of {self.testData.outcome} between {self.testData.predictor} groups."

    def execute(self):
        result = stats.f_oneway(*self.testData.valueList)
        
        returnValue = ComparisonTestResult()
        returnValue.test = self.name
        returnValue.statistic = result.statistic
        returnValue.pvalue = result.pvalue
        
        returnValue.setConclusion(self.testData)
        
        if result.pvalue <= self.testData.levelOfSignificance:
            returnValue.postHoc = TukeysTest(self.testData).execute()

        return returnValue