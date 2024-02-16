from scipy import stats

from src.services.comparison.statisticsTest import ComparisonStatisticsTest
from src.services.assumptions.normality.result import NormalityResult

class ShapiroWilkTest(ComparisonStatisticsTest):
    name = "Shapiro-Wilk Test"

    def execute(self):
        result: NormalityResult = NormalityResult()
        
        result.test = self.name
        result.passed = True
        result.statistics = {}
        result.pvalues = {}
        result.conclusions = {}

        for column in self.testData.columns:
            shapiro = stats.shapiro(self.testData.valueDict[column])
            
            if (shapiro.pvalue < 0.05):
                result.passed = False

            result.statistics[column] = shapiro.statistic
            result.pvalues[column] = shapiro.pvalue
            
            if result.passed:
                result.conclusions[column] = f"The Shapiro-Wilk test results indicate a p-value of {shapiro.pvalue}. Since this value is above the significance theshold of 0.05, we can conclude that there's no significant departure from normality in {self.testData.outcome} of the {column} group."
            else:
                result.conclusions[column] = f"The Shapiro-Wilk test results indicate a p-value of {shapiro.pvalue}. Since this value is below the significance theshold of 0.05, we can conclude that there's a significant departure from normality in {self.testData.outcome} of the {column} group."

        return result