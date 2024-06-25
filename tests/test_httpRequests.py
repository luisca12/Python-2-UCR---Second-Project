import unittest
import os
import logging


from src.functions import mkdir
from src.log import logConfiguration
from src.httpRequests import getToken, imageNumThread

infoLog = logging.getLogger('infoLog')

class TestGetToken(unittest.TestCase):
    
    pass

class TestimageNumThread(unittest.TestCase):
    def test_DownloadImage(self):
        mkdir()
        Token = getToken()
        imageNumber = 4
        imageNumThread(Token, imageNumber)

        imageExists = os.path.exists('images/image_1.jpg')
        self.assertTrue(imageExists)

# if __name__ == '__main__':
#     unittest.main()