from redis import Redis
from rq import Queue

_redis: Redis | None = None
_queue: Queue | None = None

def get_redis() -> Redis:
    global _redis
    if _redis is None:
        # Use docker service name, not localhost
        _redis = Redis(host="redis", port=6379)
    return _redis

def get_queue(name: str = "default") -> Queue:
    global _queue
    if _queue is None:
        _queue = Queue(name, connection=get_redis())
    return _queue