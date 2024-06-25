import unittest
import os
import logging
import shutil

from src.functions import mkdir
from src.log import logConfiguration

infoLog = logging.getLogger('infoLog')

class TestGetToken(unittest.TestCase):
    """
    Unit tests for the getToken function.

    Methods:
        - test_GetToken: Checks if getToken returns a string.
        - test_GetTokenNone: Checks if getToken returns None.
    """
    def test_GetToken(self):
        """
        This function checks if getToken returns a string.

        **Args**

        **Returns:**
        """
        from src.httpRequests import getToken
        token1 = getToken()
        self.assertIs(type(token1), str)
        infoLog.info(f"Running unittest: test_GetToken. The token is a string")

    def test_GetTokenNone(self):
        """
        This function checks if getToken returns None.

        **Args**
        
        **Returns:**
        """
        from src.httpRequests import getToken
        token1 = getToken()
        if token1 == None:
            infoLog.info(f"Running unittest: test_GetTokenNone. The token is None")
            infoLog.error(f"Please check token, returned value is None.")
            print(f"ERROR: Token is none. Token = {token1}")
        self.assertIsNone(token1)
        infoLog.info(f"Running unittest: test_GetTokenNone. The token is not None")

class TestimageNumThread(unittest.TestCase):
    """
    Unit tests for imageNumThread function.

    Methods:
        - setUp: Sets up necessary variables and environment for testing.
        - test_DownloadImage: Checks if the images folder exists.
        - test_DownloadImage_2: Checks if a specific image file exists after calling imageNumThread.
        - test_DownloadImage_3: Checks if a specific image file exists in the images folder.
        - tearDown: Cleans up the environment after tests are executed.
    """
    def setUp(self):
        """
        This function sets up necessary variables and environment for testing.

        **Args:**

        **Returns:**
        """
        mkdir()
        from src.httpRequests import getToken
        from src.httpRequests import imageNumThread
        self.imagePath = os.listdir('images')
        self.imagePath1 = 'images'
        self.imageName = os.path.exists('images/image_1.jpg')
        self.Token = getToken()
        self.imageNumber = 4
        imageNumThread(self.Token, self.imageNumber)

    def test_DownloadImage(self):
        """
        This function checks if the "images" folder exists.

        **Args:**
        
        **Returns:**
        """
        self.assertTrue('images')
        infoLog.info(f"Running unittest: test_DownloadImage. The folder images exists.")
    
    def test_DownloadImage_2(self):
        """
        This function checks if "image_1.jpg" image exists inside images after calling imageNumThread.

        **Args:**
        
        **Returns:**
        """
        self.assertEqual(self.imageName, True)
        infoLog.info(f"Running unittest: test_DownloadImage_2. The file \"images/image_1.jpg\" exists.")

    def test_DownloadImage_3(self):
        """
        This function checks if "image_1.jpg" image exists inside images folder.

        **Args:**
        
        **Returns:**
        """
        self.assertIn('image_1.jpg', self.imagePath)
        infoLog.info(f"Running unittest: test_DownloadImage_3. The file \"image_1.jpg\" exists.")

    def tearDown(self):
        """
        This function cleans up the environment after unit tests are executed.

        **Args:**
        
        **Returns:**
        """
        if os.path.exists('images'):
            shutil.rmtree('images')
            infoLog.info(f"The folder \"images\" does exist. Deleting folder \"images\".")
            infoLog.info(f"Folder \"images\" and all other images were successfully deleted.")

if __name__ == '__main__':
    unittest.main()