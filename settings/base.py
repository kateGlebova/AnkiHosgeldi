import logging.config
import os

basedir = os.path.abspath(os.path.dirname(__file__))

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
        "parse_log": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "full",
            "level": "INFO",
            "filename": basedir + '/parse.log'
        },
        "console": {
            "class": "logging.handlers.StreamHandler",
            "formatter": "brief",
            "level": "WARNING"
        }
    },
    "loggers": {
        "mail_logger": {
            "level": "INFO",
            "handlers": [
                "mail_log"
            ]
        },
        "parse_logger": {
            "level": "ERROR",
            "handlers": [
                "parse_log"
            ]
        },
        "root": {
            "level": "DEBUG",
            "handlers": [
                "console"
            ]
        },
    }
}

logging.config.dictConfig(config_dict)