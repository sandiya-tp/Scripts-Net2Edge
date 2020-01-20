import logging
import sys
import inspect
import traceback


#Class for logging various info
class DebugLogger:
    handler = ""
    formatter = ""
    logger = ""
    filename = ""
    
    #params - name of file to which log info should be written
    #return - none
    def __init__(self, doc_name):
        self.logger = logging.getLogger('Y1731')
        self.filename = doc_name
        self.handler = logging.FileHandler(self.filename)
        self.formatter = logging.Formatter('[%(asctime)s] - %(levelname)s - [%(filename)s : %(funcName)s : %(lineno)d] - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        self.logger.setLevel(logging.DEBUG)
    
    #Method to log info messages
    #params - message to log
    #return - none    
    def log_info(self,message):
        frame = inspect.currentframe()
        stack_trace = traceback.format_stack(frame)
        message = message + "\n" + inspect.stack()[1][1] + " : " + inspect.stack()[2][3] + " : " + inspect.stack()[1][3] + " : " + inspect.stack()[0][3] 
        self.logger.info(message)
       
    #Method to log errors
    #params - none
    #return - none
    def log_error(self):
        self.logger.exception('')        
    
        
    #Method to print messages to console
    #params - message to print
    #return - none
    def log_print(self,message):
        sys.stdout.write(message)

    #Method to log exceptions and terminate execution
    #params - none
    #return - none
    def log_error_and_exit(self):
        self.logger.exception('')  
        sys.exit()
        
    #Method to print the results of testcases to console
    #params - message to print
    #return - none
    def log_result(self,message):
        sys.stdout.write("\n"+"*"*50+ "\n")
        sys.stdout.write(message)
        sys.stdout.write("\n"+"*"*50+ "\n") 
	sys.stdout.flush() 
    
    def bannerInfo(self, message, level):
        global test_result_flag
        if level == 'INFO':
	  sys.stdout.write("\n"+"*"*50+ "\n")
          sys.stdout.write("<INFO>" + message + "</INFO>")
          sys.stdout.write("\n"+"*"*50+ "\n")
	  sys.stdout.flush()
        elif level == 'ERROR':
	  sys.stdout.write("\n"+"*"*50+ "\n")
          sys.stdout.write("<ERROR>" + message + "</ERROR>")
          sys.stdout.write("\n<FAILED>" + message + "</FAILED>")
          sys.stdout.write("\n"+"*"*50+ "\n")
	  sys.stdout.flush()
          test_result_flag = 0
        elif level == 'RESULT':
          sys.stdout.write("\n"+"*"*50+ "\n")
          sys.stdout.write("<RESULT>" + message + "</RESULT>")
          sys.stdout.write("\n"+"*"*50+ "\n")
	  sys.stdout.flush()

