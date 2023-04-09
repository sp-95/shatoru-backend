import logging
import sys
from logging import LogRecord
from typing import Any, Dict

from loguru import logger

from shatoru_backend.config import DEBUG_MODE, LOG_PATH


class InterceptHandler(logging.Handler):
    def emit(self, record: LogRecord) -> None:
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back or frame
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )


class LogConfig:
    @staticmethod
    def formatter(record: Dict[str, Any]) -> str:
        FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: ^8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"  # noqa: E501
        if record["extra"].get("tag", None):
            FORMAT += " - [<magenta>{extra[tag]}</magenta>]"
        if record["extra"].get("session_id", None):
            FORMAT += " - [<magenta>{extra[session_id]}</magenta>]"
        FORMAT += " - <level>{message}</level>\n"

        return FORMAT

    @staticmethod
    def setup() -> None:
        level = "DEBUG" if DEBUG_MODE else "INFO"

        # === Intercept everything at the root logger ===
        logging.root.handlers = [InterceptHandler()]
        logging.root.setLevel(level)

        # === Remove every other logger's handlers
        # and propagate to root logger ===
        for name in logging.root.manager.loggerDict.keys():  # type: ignore
            logging.getLogger(name).handlers = []
            logging.getLogger(name).propagate = True

        # === Log to terminal ===
        logger.configure(
            handlers=[
                {
                    "sink": sys.stdout,
                    "level": level,
                    "format": LogConfig.formatter,
                },
            ],
        )

        # === Log to specific log files ===
        levels = ["critical", "error", "warning", "info"]
        if DEBUG_MODE:
            levels.append("debug")

        for lvl in levels:
            logger.add(
                LOG_PATH / f"{lvl}.log",
                level=lvl.upper(),
                format=LogConfig.formatter,
                rotation="10MB",
            )


log_config = LogConfig()
