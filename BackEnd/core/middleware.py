import time

from fastapi import Request

from core.logging import setup_logger

logger = setup_logger(__name__)


async def logging_middleware(
    request: Request,
    call_next,
):
    start_time = time.time()

    logger.info(
        f"Incoming Request | {request.method} {request.url.path}"
    )

    try:

        response = await call_next(request)

        process_time = time.time() - start_time

        logger.info(
            f"Completed | {request.method} {request.url.path} | "
            f"Status: {response.status_code} | "
            f"Time: {process_time:.2f}s"
        )

        return response

    except Exception:

        process_time = time.time() - start_time

        logger.exception(
            f"Failed | {request.method} {request.url.path} | "
            f"Time: {process_time:.2f}s"
        )

        raise