from helpers import logging_wfs
from settings import paths_attributes
import logging

debug_file = paths_attributes.DEBUG_OUTPUT_FOLDER / "log.txt"
filehandler = logging.FileHandler(debug_file)
logging = logging_wfs.InitialLogging().set_up_logger_std("debug", logger_name=__name__).logger
logging.handlers.clear()
logging.addHandler(filehandler)



logging.debug("Start of the program")

def factorial(n): 
    logging.debug('Start of factorial(%s%%)' % (n)) 
    total = 1 
    for i in range(1, n+1):
        total *= i 
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n)) 
    return total 
print(factorial(5)) 
logging.debug('End of program')