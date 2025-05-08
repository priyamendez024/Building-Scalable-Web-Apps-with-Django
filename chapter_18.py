
# Chapter 18: Monitoring, Logging & Observability

# Example for logging setup with ELK Stack
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'elk': {
            'level': 'DEBUG',
            'class': 'logging.handlers.SocketHandler',
            'host': 'elk-host',
            'port': 12345,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['elk'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
    