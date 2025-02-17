from models.model import LogStatment
from utils.db import insert_batch
from utils.logger import logger
from uuid import uuid4

def process_pglog(logs: list[LogStatment]):
    job_id = str(uuid4())
    try:
        logger.debug(f'JOB [process_pglog][id={job_id}][docs={len(logs)}]: ', extra={'logs': logs})

        # convert list of dict to list of tuple for insert batch
        def to_tuple(doc):
            return (
                doc.query,
                doc.max_exec_time,
                doc.rows,
                doc.datname,
                doc.usename,
                doc.application_name,
                doc.client_addr,
                doc.backend_type,
                doc.created_at
            )
        
        records = list(map(to_tuple, logs))

        insert_query = """
            INSERT INTO pg_logs (query, max_exec_time, rows, datname, usename, application_name, client_addr, backend_type, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        insert_batch(insert_query, records)
    except Exception as ex:
        logger.error(f'Exception: JOB [process_pglog][id={job_id}] {str(ex)}')