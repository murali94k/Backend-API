import logging
import os


def get_logger(logger_name: str):
    logger = logging.getLogger(name=logger_name)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - '
                                  '%(funcName)s - %(lineno)s %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    if os.environ.get("LOG_LEVEL"):
        logger.setLevel(os.environ['LOG_LEVEL'].upper())
    else:
        logger.setLevel(logging.DEBUG)
    return logger
