import sys
import os
# Add the parent directory to Python path so we can import modules
sys.path.append('/app')

from rq import Worker
from rq_base import get_queue, get_redis
import time

def main() -> None:
    # Redis startup time
    time.sleep(10)
    queue = get_queue()
    redis_conn = get_redis()
    print("Starting RQ worker...")
    Worker([queue], connection=redis_conn).work()

if __name__ == "__main__":
    main()
