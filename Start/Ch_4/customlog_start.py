# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from
def another_func():
    logging.debug("This is a debug level message")

# set the output file and debug level, and
# TODO: use a custom formatting specification

fmtstr = "%(asctime)s : %(levelname)s : %(funcName)s Line:%(lineno)d %(message)s"
datestr = "%m/%d/%Y %I:%M:%S %P"
extdata = {"user" : "waleed"}
logging.basicConfig(filename="output_test.log", level=logging.DEBUG,
                    format=fmtstr, datefmt=datestr) 

logging.info("This is an info-level log message")
logging.warning("This is a warning-level message")
another_func()
