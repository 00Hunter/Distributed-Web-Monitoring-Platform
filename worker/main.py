import asyncio
from models import CheckJob , RequestType
from checkers.httpsCheck import run
from checkers.ssl_worker import extract_host_name,get_cert_expiry

async def main():
    hostname,port=extract_host_name("https://www.linkedin.com/feed/")
    result=get_cert_expiry(hostname,port,10)
    # job=CheckJob(
    #     monitor_id="1",
    #     url="https://www.google.com",
    #     timeout_seconds=10,
    #     request_type=RequestType.HTTP
    # )

    # job2=CheckJob(
    #     monitor_id="2",
    #     url="https://this-website-does-not-exist-123456.com",
    #     expected_status=404,
    #     timeout_seconds=10,
    #     request_type=RequestType.SSL
    # )

    # result=await run(job2)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())