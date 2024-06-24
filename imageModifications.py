from PIL import Image
from PIL import ImageFilter

import logging.config

infoLog = logging.getLogger('infoLog')

def blackWhite(image):
    with Image.open(f"images/{image}") as imageOut:
        imageOut = imageOut.convert('L')
        imageOut.save(f"images/{image}")
    return image

def transposeIMG(image):
    with Image.open(f"images/{image}") as imageOut:
        imageOut = imageOut.transpose(Image.FLIP_LEFT_RIGHT)
        imageOut.save(f"images/{image}")
    return image

def blurIMG(image):
    with Image.open(f"images/{image}") as imageOut:
        imageOut = imageOut.filter(ImageFilter.BLUR)  
        imageOut.save(f"images/{image}")
    return image

def rotate90(image):
    with Image.open(f"images/{image}") as imageOut:
        imageOut = imageOut.rotate(90)
        imageOut.save(f"images/{image}")
    return image