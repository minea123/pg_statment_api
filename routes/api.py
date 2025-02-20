from fastapi import APIRouter, status, Request, BackgroundTasks, Response, HTTPException
from models.model import LogStatment
from utils.custom_log import logging
from utils.api_error_handler import handle_api_error
from jobs.process_pglog import process_pglog

logger = logging.getLogger(__name__)

# Create an API router
router = APIRouter()

# Define routes under the router
@router.post("/pgstatments", status_code=status.HTTP_200_OK)
async def create_pg_log(log_statments: list[LogStatment], request: Request, background_tasks: BackgroundTasks, response: Response):
    try:
        if len(log_statments) == 0:
            raise HTTPException(status_code=400, detail="No data provided")
        background_tasks.add_task(process_pglog, log_statments)
    except Exception as e:
        return handle_api_error(request, e)