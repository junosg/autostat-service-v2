from scipy import stats

from src.services.comparison.statisticsTest import ComparisonStatisticsTest
from src.services.comparison.postHocs.result import PostHocsComparisonTestResult

class TukeysTest(ComparisonStatisticsTest):
    name = "Tukey's Test"

    def execute(self):
        result = stats.tukey_hsd(*self.testData.valueList)
        
        tukey: dict[str, PostHocsComparisonTestResult] = {}

        for leftIndex, leftColumn in enumerate(self.testData.columns):
            for rightIndex, rightColumn in enumerate(self.testData.columns):
                if (leftIndex != rightIndex):
                    key = leftColumn +"-" + rightColumn
                    tukey[key] = PostHocsComparisonTestResult()
                    tukey[key].statistic = result.statistic[leftIndex][rightIndex]
                    tukey[key].pvalue = result.pvalue[leftIndex][rightIndex]
                    
                    tukey[key].setConclusion(self.testData, leftColumn, rightColumn)

        returnValue = {
            "test": self.name,
            "result": tukey
        }

        return returnValue