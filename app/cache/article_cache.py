import json
from functools import wraps
from aiocache import Cache
from fastapi import HTTPException


def cache_response(ttl: int = 300, namespace: str = "articles"):
    """
    Caching decorator for FastAPI endpoints to cache article data.

    ttl: Time to live for the cache in seconds.
    namespace: Namespace for cache keys in Redis.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Assuming 'article_id' is provided as a query param or URL param
            user = kwargs.get('user')

            # Cache key will be based on article_id and user_id
            cache_key = f"{namespace}:article:{user.id}"
            # Set up Redis cache
            cache = Cache.REDIS(endpoint="localhost", port=6379, namespace=namespace)

            # Try to retrieve data from cache
            cached_value = await cache.get(cache_key)
            if cached_value:
                return json.loads(cached_value)  # Return cached data

            # Call the actual function if cache is not hit
            response = await func(*args, **kwargs)
            try:
                response_dict = response.dict() if hasattr(response, "dict") else response
                # Store the response in Redis with a TTL
                await cache.set(cache_key, json.dumps(response_dict), ttl=ttl)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error caching data: {e}")

            return response
        return wrapper
    return decorator
