from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
from uuid import uuid4
from utils.logger import logger
from starlette.middleware.base import BaseHTTPMiddleware
from config import env

class CheckApiKey(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        key = request.headers.get('X-API-KEY')
        if key is None or key == '' or key not in env.API_KEYS:
            return Response(
                content=f"Invalid api key",
                status_code=401,
            )

        return await call_next(request)