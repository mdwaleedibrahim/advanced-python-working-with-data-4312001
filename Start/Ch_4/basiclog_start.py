# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging

# TODO: Use basicConfig to configure logging
logging.basicConfig(level=logging.DEBUG, filename='output.log', filemode='w')
# TODO: Try out each of the log levels
logging.debug("This is a debug message")
logging.info("This is a information message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")

# TODO: Output formatted strings to the log
x = 'string'
y=10
logging.info(f"THis is a {x} variable and an int: {y}")
