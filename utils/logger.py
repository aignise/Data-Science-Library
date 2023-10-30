import logging

def configure_logging(level=logging.INFO):
    """Configure the logging settings for the library."""
    logging.basicConfig(level=level)

def log_message(message, level=logging.INFO):
    """Log a message at the specified log level."""
    if level == logging.DEBUG:
        logging.debug(message)
    elif level == logging.INFO:
        logging.info(message)
    elif level == logging.WARNING:
        logging.warning(message)
    elif level == logging.ERROR:
        logging.error(message)
    elif level == logging.CRITICAL:
        logging.critical(message)
    else:
        logging.info(message)
