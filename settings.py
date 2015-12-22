import os, logging

#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

print 'BASE_DIR={0}'.format(BASE_DIR)

DEBUG = True
UNIX = True
PORT = 8000

if UNIX:
    RESOURCE_ROOT='/opt/www/pytest/'
else:
    RESOURCE_ROOT='c:/opt/var/www/pytest/'


DATABASE_URL = 'mysql://root:justdoit@localhost/pytest'
    
LOGGING = {
    'version': 1,
    #'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s] %(levelname)s [%(module)s:%(lineno)s] - %(message)s'
        },
    },
           
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'debug.logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(RESOURCE_ROOT,'logs/debug.log'),
            'formatter': 'simple',
        },
        'info.logfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(RESOURCE_ROOT,'logs/info.log'),
            'formatter': 'simple',
        },
    },
           
    'loggers': {
        'debug_logger': {
            'handlers': ['debug.logfile', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'info_logger': {
            'handlers': ['info.logfile', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        
        'pytest': {
            'handlers': ['debug.logfile', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },       
}
