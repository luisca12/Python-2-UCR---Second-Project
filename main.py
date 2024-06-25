from functions import mkdir

import os
import logging.config

def main():
    mkdir()
    from functions import checkIsDigit, checkYNInput
    from strings import greetingString,menuString,inputErrorString,newUserString
    from log import logConfiguration
    from httpRequests import getToken, sendEmail, imageNumThread
    from imageModifications import blackWhite, transposeIMG, blurIMG, rotate90
    greetingString()
    logging.config.dictConfig(logConfiguration)
    infoLog = logging.getLogger('infoLog')
    modLog = logging.getLogger('userLog')

    while True:  
        menuString()
        selection = input("Please choose a number from 1 to 4: ")
        if checkIsDigit(selection):
            if int(selection) >= 5 or int(selection) <= 0:
                print("Only numbers from 1 to 4 are accepted.")
                os.system("PAUSE")
                os.system("CLS")
            if selection == "1":
                token = getToken()
                if token:
                    while True:
                        os.system("CLS")
                        menuString()
                        imageNumInt = input("Please choose the amount of images that you want to select: ")
                        if checkIsDigit(imageNumInt):
                            if int(imageNumInt) > 10 or int(imageNumInt) <= 0: 
                                print("Only numbers from 1 to 10 are accepted.")
                                os.system("PAUSE")
                            else:
                                imageNumThread(token, imageNumInt)
                                break
                        else:
                            infoLog.error(f"Wrong input in the option#1, input: {imageNumInt}")
                            inputErrorString()
                else:
                    print("Failed to obtain a valid token. Please try again.")
                    print(f"Current token: {token}")
            if selection == "2":
                imgSource = 'images'
                imgFiles = os.listdir(imgSource)
                for i, image in enumerate(imgFiles):
                    while True:
                        modifyIMG = input(f"Do you want to modify the image number {i + 1}? (y/n):")
                        if checkYNInput(modifyIMG):
                            if modifyIMG == "y":
                                modLog.info(f"\nThe image number {i + 1} was modified with the following:")
                                while True:
                                    BW = input(f"Do you want to make the image black and white? (y/n):")
                                    if checkYNInput(BW):
                                        if BW == "y":
                                            image = blackWhite(image)
                                            modLog.info(f"\tBlack and White")
                                            break
                                        else:
                                            break
                                    else:
                                        print(f"Invalid input: Please enter \"y\" or \"n\"")

                                while True:
                                    transpose = input(f"Do you want to transpose the image? (y/n):")
                                    if checkYNInput(transpose):
                                        if transpose == "y":
                                            image = transposeIMG(image)
                                            modLog.info(f"\tTranspose")
                                            break
                                        else:
                                            break
                                    else:
                                        print(f"Invalid input: Please enter \"y\" or \"n\"")
                            
                                while True:
                                    blur = input(f"Do you want to blur the image? (y/n):")
                                    if checkYNInput(blur):
                                        if blur == "y":
                                            image = blurIMG(image)
                                            modLog.info(f"\tBlur")
                                            break
                                        else:
                                            break
                                    else:
                                        print(f"Invalid input: Please enter \"y\" or \"n\"")
            
                                while True:
                                    rotate = input(f"Do you want to rotate 90 degress the image? (y/n):")
                                    if checkYNInput(rotate):
                                        if rotate == "y":
                                            image = rotate90(image)
                                            modLog.info(f"\tRotate 90 degress")
                                            break
                                        else:
                                            break
                                    else:
                                        print(f"Invalid input: Please enter \"y\" or \"n\"")
                                break 
                            else:
                                break
                        else:
                            print(f"Invalid input: Please enter \"y\" or \"n\"")    
            if selection == "3":
                userEmail = input("Please enter your email:")
                sendEmail(userEmail)
            if selection == "4":
                break
        else:
            infoLog.error(f"Wrong option chosen in the menu: {selection}")
            inputErrorString()
            os.system("CLS")
   
if __name__ == "__main__":
    main()
