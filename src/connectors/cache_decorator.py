from functools import wraps
from typing import Callable
from src.init import redis_manager


def cache_decorator(seconds: int = None):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            key = f"{func.__module__}:{func.__name__}:{','.join(kwargs.keys())}"
            query_params = "&".join([f"{k}={v}" for k, v in kwargs.items()])
            full_key = f"{key}?{query_params}" if query_params else key
            cached_value = await redis_manager.get(full_key)
            if cached_value:
                return cached_value
            result = await func(*args, **kwargs)
            await redis_manager.set(full_key, str(result), expire=seconds)
            return result

        return wrapper

    return decorator
