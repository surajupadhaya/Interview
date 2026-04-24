import datetime
import sys
import logging
from lark import logger
from tenacity import before_sleep_log, retry, stop_after_attempt, wait_fixed
#import functools

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def checker(func):
    def wrapper(*args, **kwargs):
        try:
            logging.info("Hey this is checker starting at %s", datetime.datetime.now())
            result = func(*args, **kwargs)
            if result == 0:
                logging.info("This is the end of checker %s", datetime.datetime.now())
            else:
                raise ValueError("Function did not return 0")
            return result
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            sys.exit(1)
    return wrapper


@checker
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2), before_sleep=before_sleep_log(logger, logging.WARNING))
def helloworld(name="World"):
    logging.info(f"Hello, {name}!")
    return 1

r=helloworld("Alice")
print(r)