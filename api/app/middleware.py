import logging
import time

from fastapi import Request

logger = logging.getLogger("app.access")


async def log_requests(request: Request, call_next):
    # Middleware so'rov router'ga yetmasdan oldin ishga tushadi. `call_next(request)`
    # so'rovni keyingi qatlamlarga (router, dependency'lar, handler) uzatadi va
    # tayyor javobni qaytaradi: shu chaqiruvdan OLDIN va KEYIN o'z kodingizni yozing.

    start = time.perf_counter()
    response = await call_next(request)
    duration_ms = (time.perf_counter() - start) * 1000

    # TODO(human): logger.info(...) bilan bitta qator yozing: metod, yo'l, status kodi
    # va duration_ms. Natija taxminan shunday bo'lsin: "POST /jobs 201 3.4ms".
    return response
