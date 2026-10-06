import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import models  # noqa: F401  (jadval Base.metadata'ga ro'yxatdan o'tishi uchun)
from app.db import Base, engine
from app.middleware import log_requests
from app.routers import health, jobs

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    # Ishga tushganda jadvallar yo'q bo'lsa yaratadi (migratsiyalar Kun 03'da).
    Base.metadata.create_all(engine)
    yield


app = FastAPI(title="mini-storytime API", lifespan=lifespan)
app.middleware("http")(log_requests)
app.include_router(health.router)
app.include_router(jobs.router)
