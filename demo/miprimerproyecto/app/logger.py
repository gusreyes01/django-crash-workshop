import logging
import logging.handlers
from datetime import datetime

from django.conf import settings

# Rotate the log file once per week on Sunday (when = W6), and keep 180 days of
# logs (backupCount = 26 weekly files).


employee_logger = logging.getLogger('EmployeeLogger')
employee_logger.addHandler(
    logging.handlers.TimedRotatingFileHandler(settings.LOG_LOCATION + 'employee_log', when="W6",
                                              backupCount=26))



class EmployeeLogger(object):
    @classmethod
    def log(cls, event):
        employee_logger.setLevel(logging.INFO)
        employee_logger.info(("%s : %s") % (datetime.now().isoformat(), event))

    @classmethod
    def error(cls, event):
        employee_logger.setLevel(logging.ERROR)
        employee_logger.error(("%s : %s") % (datetime.now().isoformat(), event))
