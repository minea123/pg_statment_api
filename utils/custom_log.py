import logging
from logging.handlers import TimedRotatingFileHandler
from config.logger import FlexibleFormatter

# Log file settings
LOG_FILE = "logs/fastapi.log"
LOG_RETENTION_DAYS = 1

# Create a rotating file handler (daily rotation)
file_handler = TimedRotatingFileHandler(
    LOG_FILE, when="midnight", interval=1, backupCount=LOG_RETENTION_DAYS, encoding="utf-8"
)
file_handler.suffix = "%Y-%m-%d"

# Console handler
console_handler = logging.StreamHandler()

# Custom log format (handles optional `extra_info`)
formatter = FlexibleFormatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Configure root logger
logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, console_handler])