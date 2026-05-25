import httpx
import time
from models import CheckJob,CheckResult

async def run(job:CheckJob) -> CheckResult:
    start=time.monotonic()

    try:
        async with httpx.AsyncClient(timeout=job.timeout_seconds) as client:
            response = await client.get(job.url)
            end=time.monotonic()
            return CheckResult(is_up=response.status_code==job.expected_status,latency_ms= int((end - start) * 1000))

    except Exception as e:
        return CheckResult(is_up=False,latency_ms=0,error=str(e))