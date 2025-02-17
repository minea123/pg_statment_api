import logging
from logging.handlers import TimedRotatingFileHandler
from config.logger import FlexibleFormatter

def make_record_with_extra(self, name, level, fn, lno, msg, args, exc_info, func=None, extra=None, sinfo=None):
    record = original_makeRecord(self, name, level, fn, lno, msg, args, exc_info, func, extra, sinfo)
    record._extra = extra
    return record

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
original_makeRecord = logging.Logger.makeRecord
logging.Logger.makeRecord = make_record_with_extra

formatter = FlexibleFormatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Configure root logger
logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, console_handler])