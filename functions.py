from log import logConfiguration

import traceback
import os
import logging.config

infoLog = logging.getLogger('infoLog')

def checkIsDigit(input_str):
    """
    This function checks if the provided string is a digit.

    **Args:**
        input_str: The string to be checked.
        
    **Returns:**
        bool: True if the string is a digit, False otherwise.
    """
    try:
        infoLog.info(f"String successfully validated selection number {input_str}, from checkIsDigit function.")
        return input_str.strip().isdigit()
    
    except Exception as error:
        infoLog.error(f"Invalid option chosen: {input_str}, error: {error}")
        infoLog.error(traceback.format_exc())

def mkdir():
    """
    This function creates directories for logs and images if they do not already exist.

    **Args:**
        
    **Returns:**
    """
    infoLog = logging.getLogger('infoLog')
    path = "logs"
    path1 = "images"
    if not os.path.exists(path):
        try:
            os.mkdir(path)
            infoLog.info(f"Path \"{path}\" wasn't found. New folder named \"{path}\" was created")
        except Exception as Error:
            print(f"ERROR: Wasn't possible to create new folder \"{path}\"")
            print(traceback.format_exc())
            infoLog.error(f"ERROR: Wasn't possible to create new folder \"{path}\"")
            infoLog.error(traceback.format_exc())
    if not os.path.exists(path1):
        try:
            os.mkdir(path1)
            infoLog.info(f"Path1 \"{path1}\" wasn't found. New folder named \"{path1}\" was created")
        except Exception as Error:
            print(f"ERROR: Wasn't possible to create new folder \"{path1}\"")
            print(traceback.format_exc())
            infoLog.error(f"ERROR: Wasn't possible to create new folder \"{path1}\"")
            infoLog.error(traceback.format_exc())
   
def checkYNInput(stringInput):
    """
    This function checks if the provided string input is either 'y' or 'n', case insensitive.

    **Args:**
        stringInput: The string to be checked.
    **Returns:**
        bool: True if the string is 'y' or 'n' (case insensitive), False otherwise.
    """
    return stringInput.lower() == 'y' or stringInput.lower() == 'n'