from dotenv import load_dotenv
import os

load_dotenv()

MODE: str = os.getenv('MODE')
DB_USERNAME: str = os.getenv('DB_USERNAME')
DB_PASSWORD: str = os.getenv('DB_PASSWORD')
DB_NAME: str = os.getenv('DB_NAME')
DB_HOST: str = os.getenv('DB_HOST')  # either 'localhost' or Unix socket path
DB_PORT: str = os.getenv('DB_PORT')
API_KEYS: list[str] = (os.getenv('API_KEYS', '') or '').split(',')