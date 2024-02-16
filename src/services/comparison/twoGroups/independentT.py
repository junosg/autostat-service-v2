from scipy import stats

from src.services.statisticsTest import StatisticsTest
from src.services.comparison.result import ComparisonTestResult

from src.services.assumptions.normality.shapiroWilk import ShapiroWilkTest
from src.services.assumptions.equalVariance.levenes import LevenesTest

class IndependentTTest(StatisticsTest):
    name = "Independent T-test"
    
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
        result = stats.ttest_ind(*self.testData.valueList)
        
        returnValue = ComparisonTestResult()
        returnValue.test = self.name
        returnValue.statistic = result.statistic
        returnValue.pvalue = result.pvalue
        
        if result.pvalue > self.testData.levelOfSignificance:
            returnValue.conclusion = f"The {self.name} results indicate a p-value of {result.pvalue}. Since this value is above the significant threshold of {self.testData.levelOfSignificance}, we can conclude that there is no significant difference in {self.testData.outcome} between {self.testData.predictor} groups."
        else:
            returnValue.conclusion = f"The {self.name} results indicate a p-value of {result.pvalue}. Since this value is below the significant threshold of {self.testData.levelOfSignificance}, we can conclude that there is a significant difference in {self.testData.outcome} between {self.testData.predictor} groups."

        return returnValue