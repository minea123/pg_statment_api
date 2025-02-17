from typing import Union
from fastapi import FastAPI, Request
from fastapi import FastAPI
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from routes.api import router
from middlewares.LogRequest import LogRequest
from middlewares.CheckApiKey import CheckApiKey
from utils.logger import logger

app = FastAPI()
app.add_middleware(LogRequest)
app.add_middleware(CheckApiKey)
app.include_router(router, prefix='/api/v1')