import logging
import os


def log_handler():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        sh = logging.StreamHandler()
        logger.addHandler(sh)
        fh = logging.FileHandler(os.path.join(os.path.dirname(__file__), '../log/run.log'), encoding='utf-8')
        logger.addHandler(fh)
        fmt = '%(levelname)s  %(asctime)s - %(filename)s - %(funcName)s - %(message)s'
        log_format = logging.Formatter(fmt)
        sh.setFormatter(log_format)
        fh.setFormatter(log_format)
    return logger


log = log_handler()
