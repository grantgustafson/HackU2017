import os
from os.path import join, normpath
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import socket
import logging, logging.config

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.abspath(CURR_DIR + "/../")

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://localhost/ggustafson'
#SQLALCHEMY_DATABASE_URI = 'postgresql://nstebbins@10.6.32.216/nstebbins'



CURR_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.abspath(CURR_DIR + "/../")
LOGGING_DIR = normpath(join(APP_DIR, '../logs'))

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

assert os.path.isdir(LOGGING_DIR)

LOG_CONFIG = {'version': 1,
              'formatters': {
                  'request': {
                      'format': '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
                  },
                  'listener': {
                      'format': '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
                  }
              },
              'handlers': {
                  'stdout': {
                      'class': 'logging.StreamHandler',
                      'formatter': 'request',
                      'stream': 'ext://sys.stdout'
                  },
                  'stream': {
                      'class': 'logging.StreamHandler',
                      'formatter': 'request',
                  },
                  'log': {
                      'class': 'logging.handlers.TimedRotatingFileHandler',
                      'formatter': 'listener',
                      'filename': os.path.join(LOGGING_DIR, 'log'),
                      'when': 'midnight',
                  },
              },
              'loggers': {
                  'logger': {
                      'level': 'DEBUG',
                      'handlers': ['log', 'stdout'],
                  },
              }
            }
logging.config.dictConfig(LOG_CONFIG)
LOGGER = logging.getLogger('logger')
