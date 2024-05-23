from strings import greetingString,menuString,inputErrorString,newUserString
from log import logConfiguration
from functions import checkIsDigit, mkdir, checkYNInput
from httpRequests import getToken, imageNum

import os
import logging.config

logging.config.dictConfig(logConfiguration)
infoLog = logging.getLogger('infoLog')

def main():
    os.system("CLS")
    mkdir()

    while True:
        greetingString()
        menuString()
        selection = input("Please choose a number from 1 to 4: ")
        if checkIsDigit(selection):
            if int(selection) >= 5 or int(selection) <= 0:
                print("Only numbers from 1 to 4 are accepted.")
                os.system("PAUSE")
            if selection =="1":
                token = getToken()
                if token:
                    print(f"{token}")
                    imageNumInt = input("Please choose the amount of images that you want to select: ")
                    imageNumInt = int(imageNumInt)
                    imageNum(token, imageNumInt)
                    break
                else:
                    print("Failed to obtain a valid token. Please try again.")
                    print(f"Current token: {token}")
        else:
            infoLog.error(f"Wrong option chosen in the menu: {selection}")
            inputErrorString()
            os.system("CLS")
   
if __name__ == "__main__":
    main()
