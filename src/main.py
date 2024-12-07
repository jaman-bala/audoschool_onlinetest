import sys
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from pathlib import Path
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

sys.path.append(str(Path(__file__).parent.parent))

from src.init import redis_manager
from src.api.auth import router as router_auth
from src.api.images import router as router_images
from src.api.questions import router as router_questions
from src.api.tickets import router as router_tickets
from src.api.answers import router as router_answers
from src.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_manager.connect()
    FastAPICache.init(RedisBackend(redis_manager), prefix="fastapi-cache")
    yield
    await redis_manager.close()


app = FastAPI(
    docs=None,
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)

app.include_router(router_auth)
app.include_router(router_images)
app.include_router(router_tickets)
app.include_router(router_questions)
app.include_router(router_answers)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8005)
