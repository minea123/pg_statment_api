from fastapi import Request
from errors.CustomErrorHandler import CustomException

def handle_api_error(request: Request, err: Exception):
    raise CustomException('Error exception', 500, request)