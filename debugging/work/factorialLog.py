import logging
from settings import paths_attributes
from helpers import logging_wfs
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logger = logging_wfs.InitialLogging().set_up_logger_std(log_level="debug",logger_name=__name__).logger

# logging.disable(logging.DEBUG)
logger.debug('Start of program')


def factorial(n):
    logger.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logger.debug('i is ' + str(i) + ', total is ' + str(total))
    logger.debug('End of factorial(%s%%)' % (n))
    return total


print(factorial(5))
logger.debug('End of program')

