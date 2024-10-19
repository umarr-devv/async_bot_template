import os
from logging import StreamHandler, basicConfig
from logging.handlers import TimedRotatingFileHandler

from src.config import Config

LOG_FORMAT = '%(name)s | %(asctime)s | %(funcName)s | %(filename)s | %(levelname)s | %(message)s'
LOG_FILENAME = '.log'
LOG_DIR = os.getcwd() + '/logs'
LOG_INTERVAl = 7


def set_logging(config: Config):
    basicConfig(
        level=config.logging.level,
        format=LOG_FORMAT,
        handlers=[
            StreamHandler(),
            TimedRotatingFileHandler(
                filename=LOG_DIR + '/' + LOG_FILENAME,
                when='D',
                interval=LOG_INTERVAl,
                encoding='utf-8'
            )
        ]
    )
