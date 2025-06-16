import logging
import pathlib

project_root = pathlib.Path(__file__).parent.parent.resolve()


def setup_logger(name: str) -> logging.Logger:
    """Return a logger with stream and file handlers.

    Handlers are only added if the logger doesn't already have any.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        fh = logging.FileHandler(f"{project_root}/application.log")
        fh.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)
    return logger
