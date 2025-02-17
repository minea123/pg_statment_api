import logging
from logging.handlers import RotatingFileHandler

# Set up logging
logger = logging.getLogger('uvicorn')

# Set up the rotating file handler
file_handler = RotatingFileHandler('logs/fastapi.log', maxBytes=5 * 1024 * 1024, backupCount=3)  # 5 MB max size, 3 backup files

# Custom formatter that dynamically adjusts the format based on the presence of 'body'
class CustomFormatter(logging.Formatter):
    def format(self, record):
        # Check if 'body' exists in the record
        if hasattr(record, 'body'):
            self._style._fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s - Body: %(body)s'
        else:
            self._style._fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        return super().format(record)

# File formatter
file_formatter = CustomFormatter()
file_handler.setFormatter(file_formatter)

# Console formatter
console_handler = logging.StreamHandler()
console_formatter = CustomFormatter()
console_handler.setFormatter(console_formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
