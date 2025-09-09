import sys
import os
# Add the parent directory to Python path so we can import modules
sys.path.append('/app')

from task_creator.task import wait_print_count
from rq_base import get_queue
import time

def create_task():
    q = get_queue()
    result = q.enqueue(wait_print_count)
    print(f"Task enqueued: {result}")
    time.sleep(10)
    result = q.enqueue(wait_print_count)
    print(f"Task enqueued: {result}")
    
if __name__ == "__main__":
    time.sleep(15)
    create_task()