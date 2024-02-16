from typing import Annotated

from fastapi import FastAPI, File, UploadFile, HTTPException

from .controllers.test import test_router

app = FastAPI()

app.include_router(test_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/upload")
async def create_upload_file(file: UploadFile): 
    if ".xls" not in file.filename or ".xlsx" not in file.filename:
        raise HTTPException(status_code=422, detail="Item not found")

    return {"filename": file}

@app.post("/testValidation")
async def test_validation(email: str, number: int, name: str|None = None):  
    return "success"
    
    
