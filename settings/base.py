# -*- coding: utf-8 -*-

import logging.config
import os

import sys

basedir = os.path.abspath(os.path.dirname(__file__) + '/..')


newsletter_from = 'administrator@hosgeldi.com'

languages = {
    'French': u'Учить слова на французском',
    'English': u'Учить слова на английском',
    'German': u'Учить слова на немецком'
}

config_dict = {
    "version": 1,
    "formatters": {
        "brief": {
            "format": "%(levelname)-8s: %(name)-15s: %(message)s"
        },
        "full": {
            "format": "%(asctime)s %(name)-15s %(levelname)-8s %(message)s"
        }
    },
    "handlers": {
        "mail_log": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "full",
            "level": "INFO",
            "filename": basedir + '/mail.log'
        },
        "log": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "full",
            "level": "INFO",
            "filename": basedir + '/main.log'
        }
    },
    "loggers": {
        "mail_logger": {
            "level": "INFO",
            "handlers": [
                "mail_log"
            ]
        },
        "logger": {
            "level": "INFO",
            "handlers": [
                "log"
            ]
        }
    }
}

logging.config.dictConfig(config_dict)
sys.path.append(basedir)
