from fastapi import APIRouter, status, Request, BackgroundTasks
from models.model import LogStatment
from utils.custom_log import logging
from utils.api_error_handler import handle_api_error
from jobs.process_pglog import process_pglog

logger = logging.getLogger(__name__)

# Create an API router
router = APIRouter()

# Define routes under the router
@router.post("/pgstatments", status_code=status.HTTP_200_OK)
async def create_pg_log(log_statments: list[LogStatment], request: Request, background_tasks: BackgroundTasks):
    try:
        background_tasks.add_task(process_pglog, log_statments)
        return None
    except Exception as e:
        return handle_api_error(request, e)