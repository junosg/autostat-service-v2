from typing import Annotated
from fastapi import APIRouter, File, UploadFile, HTTPException, Body
import pandas as pd

from pydantic import BaseModel, ValidationError
from pydantic.functional_validators import AfterValidator

from ..requests.test import PerformTestRequest

from ..models.comparisonTestData import ComparisonTestData

from src.services.comparison.service import ComparisonService

test_router = APIRouter()

@test_router.post('/performTest')
async def perform_test(request: PerformTestRequest):
    testData = ComparisonTestData(request.data, request.levelOfSignificance, request.predictor, request.outcome, request.predictorPaired)

    test = ComparisonService(testData=testData)

    return test.analyze()