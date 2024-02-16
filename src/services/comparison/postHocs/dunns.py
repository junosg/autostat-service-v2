import numpy as np
import scikit_posthocs as sp

from src.services.comparison.statisticsTest import ComparisonStatisticsTest
from src.services.comparison.postHocs.result import PostHocsComparisonTestResult

class DunnsTest(ComparisonStatisticsTest):
    name = "Dunn's Test"

    def execute(self):
        result = sp.posthoc_dunn(self.testData.valueList, p_adjust = 'bonferroni')
        
        dunn: dict[str, PostHocsComparisonTestResult] = {}

        for leftIndex, leftColumn in enumerate(self.testData.columns):
            for rightIndex, rightColumn in enumerate(self.testData.columns):
                if (leftIndex != rightIndex):
                    key = leftColumn + "-" + rightColumn
                    dunn[key] = PostHocsComparisonTestResult()
                    dunn[key].pvalue = result.values[leftIndex][rightIndex]
                    dunn[key].setConclusion(self.testData, leftColumn, rightColumn)

        returnValue = {
            "test": self.name,
            "result": dunn
        }

        return returnValue