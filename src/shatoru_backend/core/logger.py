import logging
import sys
from functools import cache

from loguru import logger

from shatoru_backend.core.config import settings


class InterceptHandler(logging.Handler):  # pragma: no cover
    @cache
    def emit(self, record: logging.LogRecord) -> None:
        # Get corresponding Loguru level if it exists
        level: int | str
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            if frame.f_back:
                frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )


@cache
def setup_loggers() -> None:
    level = "DEBUG" if settings.DEBUG else "INFO"

    # Intercept everything at the root logger
    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel(level)

    # Remove every other logger's handlers and propagate to the root logger
    for name in logging.root.manager.loggerDict.keys():  # type: ignore
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    logger.configure(
        handlers=[{"sink": sys.stdout, "level": level, "format": settings.LOG_FORMAT}],
    )

    for level in ["critical", "error", "warning", "info", "debug"]:
        logger.add(
            settings.LOG_PATH / f"{level}.log",
            level=level.upper(),
            format=settings.LOG_FORMAT,
            rotation="10MB",
        )
