from pydantic import BaseModel , Field
from typing import Optional
from datetime import datetime,timezone
from enum import Enum

class RequestType(Enum):
    HTTP = "HTTP"
    SSL = "SSL"


class CheckJob(BaseModel):
    monitor_id:str
    url:str
    timeout_seconds:int
    request_type:RequestType
    expected_status: int = 200 

class CheckResult(BaseModel):
    is_up:bool
    latency_ms:int
    error:Optional[str]=None
    checked_at:datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
