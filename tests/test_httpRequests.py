import unittest
import os
import logging


from src.functions import mkdir
from src.log import logConfiguration

infoLog = logging.getLogger('infoLog')

class TestGetToken(unittest.TestCase):
    
    def setUp(self):
        if not os.path.exists('token'):
            os.mkdir('token')
            infoLog.info(f"The folder \"token\" does not exist. Creating folder \"token\".")

    def test_GetToken(self):
        from src.httpRequests import getToken
        token = getToken()

        self.assertIs(type(token), str)
        infoLog.info(f"Running unittest: test_GetToken. The token is a string")

    def test_GetTokenNone(self):
        from src.httpRequests import getToken
        token = getToken()

        self.assertIsNone(token)
        infoLog.info(f"Running unittest: test_GetTokenNone. The token is None")

    def tearDown(self):
        if os.path.exists('token') == True:
            os.remove('token')
            infoLog.info(f"The folder \"token\" does exist. Deleting folder \"token\".")

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
        infoLog.info(f"Running unittest: test_DownloadImage. The folder images exists.")
    
    def test_DownloadImage_2(self):
        from src.httpRequests import imageNumThread
        imageNumThread(self.Token, self.imageNumber)

        self.assertTrue(self.imageName)
        infoLog.info(f"Running unittest: test_DownloadImage_2. The file \"images/image_1.jpg\" exists.")

    def test_DownloadImage_3(self):
        from src.httpRequests import imageNumThread
        imageNumThread(self.Token, self.imageNumber)

        self.assertIn('image_1.jpg', self.imagePath)
        infoLog.info(f"Running unittest: test_DownloadImage_3. The file \"image_1.jpg\" exists.")

    def tear(self):
        if os.path.exists('images') == True:
            os.remove('images')
            infoLog.info(f"The folder \"images\" does exist. Deleting folder \"images\".")
            infoLog.info(f"Folder \"images\" and all other images were successfully deleted.")

if __name__ == '__main__':
    unittest.main()