import logging
import sys

LOGGING_FORMATTER = "%(levelname)s - %(message)s"

DebugLevelType = int


def get_logger(level: DebugLevelType = logging.DEBUG):
    logger = logging.getLogger()

    if not logger.hasHandlers():
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(LOGGING_FORMATTER)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(level)

    return logger
