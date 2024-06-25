import unittest
import os
import logging


from src.functions import mkdir
from src.log import logConfiguration

infoLog = logging.getLogger('infoLog')

class TestGetToken(unittest.TestCase):
    
    pass

class TestimageNumThread(unittest.TestCase):

    def setUp(self):
        mkdir()
        from src.httpRequests import getToken
        self.imagePath = os.listdir('images')
        self.imageName = os.path.exists('images/image_1.jpg')
        self.Token = getToken()
        self.imageNumber = 4

    def test_DownloadImage(self):
        from src.httpRequests import imageNumThread
        imageNumThread(self.Token, self.imageNumber)

        self.assertTrue('images')
    
    def test_DownloadImage_2(self):
        from src.httpRequests import imageNumThread
        imageNumThread(self.Token, self.imageNumber)

        self.assertTrue(self.imageName)

    def test_DownloadImage_3(self):
        from src.httpRequests import imageNumThread
        imageNumThread(self.Token, self.imageNumber)

        self.assertIn('image_1.jpg', self.imagePath)

    def tearDown(self):
        if os.path.exists('image_1.jpg') == True:
            os.remove('image_1.jpg')

if __name__ == '__main__':
    unittest.main()