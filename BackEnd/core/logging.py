import logging
from venv import logger


def setup_logger(name: str) -> logging.Logger:
    """
    Creates and configures a logger.
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # handler = logging.StreamHandler()
    handler = logging.StreamHandler()

    handler.setLevel(logging.INFO)

    logger.propagate = False

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger