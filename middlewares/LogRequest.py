from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from uuid import uuid4
from utils.logger import logger
from starlette.middleware.base import BaseHTTPMiddleware

class LogRequest(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid4())
        body = await request.body()
        json = body.decode("utf-8")

        logger.debug(f'Request ID {request_id}', extra={'body': json})

        res = await call_next(request)
        res.headers['X-Request-ID'] = request_id
        request.request_id = request_id
        return res
        