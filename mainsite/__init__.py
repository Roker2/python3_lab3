import logging
from django.conf import settings

if settings.DEBUG:
    logging.basicConfig(filename="debug.log", level=logging.DEBUG)  # if debug is enabled, we can see debug level
else:
    logging.basicConfig(filename="info.log", level=logging.INFO)
