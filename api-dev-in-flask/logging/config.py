import logging
from logging.config import dictConfig

DEBUG = True

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(module)s: %(levelname)s %(pathname)s:%(funcName)s:%(lineno)s %(message)s',
    }},
    'handlers': {'wsgi_syslog': {
        'class': 'logging.handlers.SysLogHandler',
        'address': '/dev/log',
        'facility': 'local7',
        'formatter':'default'
    },
        'werk_nulllog': {
            'class': 'logging.NullHandler'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi_syslog'],
        'propagate': True
    },
    'werkzeug': {
        'level': 'ERROR',
        'handlers': ['werk_nulllog'],
        'propagate': False
    }
})

