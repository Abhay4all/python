
# Logging is a means of tracking events that happen when some software runs. Logging is important for software developing, debugging, and running. If you don’t have any logging record and your program crashes, there are very few chances that you detect the cause of the problem. And if you detect the cause, it will consume a lot of time. With logging, you can leave a trail of breadcrumbs so that if something goes wrong, we can determine the cause of the problem. 
# 
# 
# 
# Why Printing is not a good option?
# Some developers use the concept of printing the statements to validate if the statements are executed correctly or some error has occurred. But printing is not a good idea. It may solve your issues for simple scripts but for complex scripts, the printing approach will fail.
# Python has a built-in module logging which allows writing status messages to a file or any other output streams. The file can contain the information on which part of the code is executed and what problems have been arisen.  
# 
# Levels of Log Message
# There are five built-in levels of the log message.  
# 
# Debug : These are used to give Detailed information, typically of interest only when diagnosing problems.
# Info : These are used to confirm that things are working as expected
# Warning : These are used an indication that something unexpected happened, or is indicative of some problem in the near future
# Error : This tells that due to a more serious problem, the software has not been able to perform some function
# Critical : This tells serious error, indicating that the program itself may be unable to continue running




import threading
import time
import logging

# Logging Levels
# CRITICAL	    50
# ERROR	        40
# WARNING	    30
# INFO	        20
# DEBUG	        10
# NOTSET	    0


# logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s](%(threadName)-9s) %(message)s')
logging.basicConfig(level=logging.DEBUG,format='%(levelname)s %(threadName)s %(message)s')

def worker():
    logging.debug('starting')
    time.sleep(2)
    logging.debug('Exiting')

for i in range(10):
    th=threading.Thread(target=worker)
    th.start()