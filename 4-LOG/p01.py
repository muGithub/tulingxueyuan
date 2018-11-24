import logging

LOG_FORMAT = "%(asctime)s=========%(levelname)s************(message)s"
logging.basicConfig(filename="tuling.log", level=logging.DEBUG, format=LOG_FORMAT)

logging.debug("debug log")
logging.critical("critical")


logging.log(logging.ERROR, "this INFO")
