import numpy as np
import scipy.stats as stats

class TestData():
    levelOfSignificance: float
    predictor: str
    outcome: str
    predictorPaired: bool
    
    valueDict: dict[str, list] = {}
    valueList: list[list] = []
    columns: list[str] = []
    
    def __init__(self, data: list, levelOfSignificance: float, predictor: str, outcome: str, predictorPaired: bool = False) -> None:
        valueDict: dict[str, list] = {}
        valueList: list[list] = []
        columns: list[str] = []

        dataNpArray: list[dict] = np.array(data)

        for item in dataNpArray:
            if item[predictor] in valueDict:
                valueDict[item[predictor]].append(item[outcome])
            else:
                valueDict[item[predictor]] = [item[outcome]]
                columns.append(item[predictor])

        for column in columns:
            valueList.append(valueDict[column])

        self.valueDict = valueDict
        self.valueList = valueList
        self.columns = columns
        self.levelOfSignificance = levelOfSignificance
        self.predictor = predictor
        self.outcome = outcome
        self.predictorPaired = predictorPaired