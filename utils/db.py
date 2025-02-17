import psycopg2
from psycopg2 import pool
from utils.custom_log import logging
from config import env

logger = logging.getLogger(__name__)

connection_pool = psycopg2.pool.SimpleConnectionPool(
    2,
    5,
    user=env.DB_USERNAME,
    password=env.DB_PASSWORD,
    host=env.DB_HOST,
    port=env.DB_PORT,
    database=env.DB_NAME
)

def insert_batch(insert_query: str, records: list[tuple]):
    conn = connection_pool.getconn()
    try:
        # Create a cursor to execute the query
        cursor = conn.cursor()
        # Execute the prepared statement for a batch of records
        cursor.executemany(insert_query, records)
        
        # Commit the transaction
        conn.commit()
        logger.debug(f"Inserted {len(records)} records.")
    except Exception as e:
        logger.error(f"Error executing batch insert: {e}")
    finally:
        # Return the connection to the pool
        connection_pool.putconn(conn)
