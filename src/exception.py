# exception handling purposes
# Search up Exception Python Documentation on google

import sys # Provides functions and variables that manipulate Python Runtime environment
# sys contains a list of directories that the interpreter will search in for the required module
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # will tell u where the exception has occured such as line and location
    file_name=exc_tb.tb_frame.f_code.co_filename # will return filename given through exception python documentation
    error_message="Error occured in python script name [{0}] line number [{1} error message [{2}]]".format()
    file_name,exc_tb.tb_lineno,str(error)

    return error_message

# created function that returns error mesage ^    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
# created class with attributes that will print error message for every instance
