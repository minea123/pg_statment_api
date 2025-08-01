from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LogStatment(BaseModel):
    queryid: int
    query: str
    max_exec_time: float
    rows: int
    datname: Optional[str] = None
    usename: Optional[str] = None
    application_name: Optional[str] = None
    client_addr: Optional[str] = None
    backend_type: Optional[str] = None
    total_plan_time: Optional[float] = 0
    max_plan_time: Optional[float] = 0
    total_exec_time: float
    created_at: str
    server_name: str = ''
    server_ip: str = ''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    