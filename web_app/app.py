import uvicorn
from pydantic import BaseModel
from typing import Optional

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from src.model import test_text

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

@app.get('/')
def read_root():
    return 'hello world'


@app.get("/rest")
def read_item(x: str):
    result = test_text(x)
    return {"number_spelled": result}

@app.get("/form")
def form_post(request: Request):
    result = " "
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})


@app.post("/form") # Post method : the browser uses this method to ask the server a response with the user's parameter
def form_post(request: Request, x: str = Form(...)): # (...) Initialization of the file object store the "num" variable
    result = test_text(x)
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})