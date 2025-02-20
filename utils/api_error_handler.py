from fastapi import Request
from errors.CustomErrorHandler import CustomException

# todo
def handle_api_error(request: Request, err: Exception):
    raise err