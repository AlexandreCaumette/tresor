import logging


def init_logger() -> logging.Logger:
    logger = logging.getLogger(__name__)

    logger.setLevel(logging.DEBUG)

    for handler in logger.handlers:
        logger.removeHandler(handler)

    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger


log = init_logger()
