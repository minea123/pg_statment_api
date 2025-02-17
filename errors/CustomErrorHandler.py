from fastapi import Request

class CustomException(Exception):
    def __init__(self, message: str, code: int, request: Request):
        self.message = message
        self.code = code
        self.request = request