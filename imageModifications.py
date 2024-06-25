from PIL import Image
from PIL import ImageFilter

import logging.config

infoLog = logging.getLogger('infoLog')

def blackWhite(image):
    """
    This function converts an image to black and white.

    **Args:**
        image: The name of the image file to be processed, located in the "images" directory.

    **Returns:**
    *    The processed image file.
    """
    with Image.open(f"images/{image}") as imageOut:
        imageOut = imageOut.convert('L')
        imageOut.save(f"images/{image}")
    return image

def transposeIMG(image):
    """
    This function transposes an image.

    **Args:**
        image: The name of the image file to be processed, located in the "images" directory.

    **Returns:**
    *    The processed image file.
    """
    with Image.open(f"images/{image}") as imageOut:
        imageOut = imageOut.transpose(Image.FLIP_LEFT_RIGHT)
        imageOut.save(f"images/{image}")
    return image

def blurIMG(image):
    """
    This function blurs an image.

    **Args:**
        image: The name of the image file to be processed, located in the "images" directory.

    **Returns:**
    *    The processed image file.
    """
    with Image.open(f"images/{image}") as imageOut:
        imageOut = imageOut.filter(ImageFilter.BLUR)  
        imageOut.save(f"images/{image}")
    return image

def rotate90(image):
    """
    This function blurs an image.

    **Args:**
        image: The name of the image file to be processed, located in the "images" directory.

    **Returns:**
    *    The processed image file.
    """
    with Image.open(f"images/{image}") as imageOut:
        imageOut = imageOut.rotate(90)
        imageOut.save(f"images/{image}")
    return image