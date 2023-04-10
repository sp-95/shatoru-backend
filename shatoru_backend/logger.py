import logging
import sys
from logging import LogRecord
from typing import Any, Dict

from loguru import logger

from shatoru_backend.config import DEBUG_MODE, LOG_PATH


class InterceptHandler(logging.Handler):
    """
    A custom logging handler that intercepts messages from the root logger and forwards
    them to Loguru for processing.

    This class extends the built-in `logging.Handler` class and overrides the `emit`
    method to translate messages to Loguru logging events.

    Methods:
        emit(record: LogRecord) -> None: Translates a LogRecord object to a Loguru
            logging event and passes it on for processing.

    Usage:
        # Create a new instance of the InterceptHandler class
        handler = InterceptHandler()

        # Add the handler to the root logger
        logging.root.handlers = [handler]

        # Configure Loguru as needed
        logger.add(...)
    """

    def emit(self, record: LogRecord) -> None:
        """
        Translate a LogRecord object to a Loguru logging event and pass it on for
        processing.

        This method overrides the `emit` method in the `logging.Handler` class and is
        called whenever a new logging message is received by the root logger.

        Args:
            record (LogRecord): A logging record object containing details about the
                logged message.
        """
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where the logged message originated
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back or frame
            depth += 1

        # Translate the log message to a Loguru event and forward it for processing.
        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )


class LogConfig:
    """Class responsible for configuring logging for the application.

    This class sets up logging for the application by intercepting all log messages and
    sending them to the Loguru logger. It sets up a console logger and file loggers for
    various logging levels (info, warning, error, critical, and debug if in debug mode).

    Methods:
        formatter(record: Dict[str, Any]) -> str: Returns the format for the log message
        setup() -> None: Sets up the logging configuration for the application.

    Usage:
        To use this class, simply call the `setup` method, which will set up the logging
        configuration for the application.
    """

    @staticmethod
    def formatter(record: Dict[str, Any]) -> str:
        """Returns the format for the log message.

        This method takes a log record as input and returns the format for the log
        message. The format includes the timestamp, log level, logger name, function
        name, line number, and message.

        Args:
            record (Dict[str, Any]): The log record.

        Returns:
            str: The format for the log message.
        """
        # Log message format
        FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: ^8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"  # noqa: E501

        # Add the message to the format
        FORMAT += " - <level>{message}</level>\n"

        return FORMAT

    @staticmethod
    def setup() -> None:
        """
        Set up logging configuration.

        This method sets up the root logger and adds handlers to it, as well as to
        specific loggers for different levels. The logging configuration is based
        on the DEBUG_MODE and the formatter specified in the `formatter` method.
        """

        # Determine logging level based on the DEBUG_MODE
        level = "DEBUG" if DEBUG_MODE else "INFO"

        # Add InterceptHandler to root logger
        logging.root.handlers = [InterceptHandler()]

        # Set logging level for root logger
        logging.root.setLevel(level)

        # Remove any other handlers from loggers and propagate to root logger
        for name in logging.root.manager.loggerDict.keys():
            logging.getLogger(name).handlers = []
            logging.getLogger(name).propagate = True

        # Configure logger with specified handlers
        logger.configure(
            handlers=[
                {
                    "sink": sys.stdout,
                    "level": level,
                    "format": LogConfig.formatter,
                },
            ],
        )

        # Add file handlers for specific log levels
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
