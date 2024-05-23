import requests
import requests.auth
import logging.config
import io
import os
from PIL import Image

infoLog = logging.getLogger('infoLog')

tokenURL = 'https://python-course.lat/image-app/api-token-auth/'
imageURL = 'https://python-course.lat/image-app/images/'
username = 'user'
password = 'python22024!'

def getToken():
    try:
        authentication = {
            'user': username,
            'password': password
        }
        response = requests.post(tokenURL, json=authentication)
        if response.status_code == 200:
            token = response.text
            infoLog.info(f"Token successfully taken. Token:{token}")
            return token
        else:
            print(f"ERROR: Failed to obtain the token. Error code: {response.status_code}")
            print(f"ERROR: {response.json()}")
            infoLog.error(f"Failed to obtain the token. Error code: {response.status_code}, {response.json()}")
            return None
    except requests.exceptions.RequestException as error:
        print(f"ERROR: {error}")
        infoLog.error(f"Failed to obtain the token. Error code: {response.status_code}, {response.json()}, error:{error}")
        return None
    except Exception as error:
        print(f"ERROR:{error}")
        infoLog.error(f"Failed to obtain the token. Error code: {response.status_code}, {response.json()}, error:{error}")
        return None

def imageNum(token, imageNumInt):
    token = token
    try:
        postHeaders = {
          'Authorization': f'Bearer {token}',
        }
        payload = {
            "cantidad" : int(imageNumInt)
        }
        response = requests.post(imageURL, headers=postHeaders, json=payload)
        if response.status_code == 200:
            image_data = response.content
            image = Image.open(image_data)
            image.show()
            print("Sucessfull")
        else:
            print(f"ERROR: Failed to obtain images. POST fail error code: {response.status_code}")
            print(f"ERROR: {response.json()}")  
            infoLog.error(f"Failed to obtain the images in the POST call(imageNum). Error code: {response.status_code}, {response.json()}")
    except requests.exceptions.RequestException as error:
        print(f"ERROR: {error}")      
        infoLog.error(f"Failed to obtain the images in the POST call(imageNum). Error code: {response.status_code}, {response.json()}, error:{error}")
    except Exception as error:
        print(f"ERROR: {error}")
        infoLog.error(f"Failed to obtain the images in the POST call(imageNum). Error code: {response.status_code}, {response.json()}, error:{error}")