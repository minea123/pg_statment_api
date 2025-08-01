from models.model import LogStatment
from utils.db import insert_batch
from utils.custom_log import logging
from uuid import uuid4

logger = logging.getLogger(__name__)

def process_pglog(logs: list[LogStatment]):
    job_id = str(uuid4())
    try:
        log_as_dict = [log.dict() for log in logs]
        logger.debug(f'JOB [process_pglog][id={job_id}][docs={len(logs)}]: ', extra={'logs': log_as_dict })

        # convert list of dict to list of tuple for insert batch
        def to_tuple(doc: LogStatment):
            return (
                doc.queryid,
                doc.query,
                doc.max_exec_time,
                doc.rows,
                doc.datname,
                doc.usename,
                doc.application_name,
                doc.client_addr,
                doc.backend_type,
                doc.created_at,
                doc.total_exec_time,
                doc.total_plan_time,
                doc.max_plan_time,
                doc.server_name,
                doc.server_ip
            )
        
        records = list(map(to_tuple, logs))

        insert_query = """
            INSERT INTO pg_logs (queryid, query, max_exec_time, rows, datname, usename, application_name, client_addr, backend_type, created_at, total_exec_time, total_plan_time, max_plan_time, server_name, server_ip)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        insert_batch(insert_query, records)
    except Exception as ex:
        logger.error(f'Exception: JOB [process_pglog][id={job_id}] {str(ex)}')