import logging
import logging.handlers
from datetime import datetime

from django.conf import settings

# Rotate the log file once per week on Sunday (when = W6), and keep 180 days of
# logs (backupCount = 26 weekly files).
api_authentication_logger = logging.getLogger('ApiAuthenticationLogger')
api_authentication_logger.addHandler(
    logging.handlers.TimedRotatingFileHandler(settings.LOG_LOCATION + 'api_authentication_log', when="W6",
                                              backupCount=26))


class ApiAuthenticationLogger(object):
    @classmethod
    def log(cls, event):
        api_authentication_logger.setLevel(logging.INFO)
        api_authentication_logger.info(("%s : %s") % (datetime.now().isoformat(), event))

    @classmethod
    def error(cls, event):
        api_authentication_logger.setLevel(logging.ERROR)
        api_authentication_logger.error(("%s : %s") % (datetime.now().isoformat(), event))
