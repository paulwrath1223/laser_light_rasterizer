"""
File function description

Desired output:
    [
        frame data: [[x, y, laser on/of], [x, y, laser on/of], etc...]
        frame data: [[x, y, laser on/of], [x, y, laser on/of], etc...]
        etc...
    ]
"""

"""
TODO:
 - convert image to black and white - DONE
 - (simplify image -> get the outline)
 - convert image to svg (scalable vector graphics)
 - convert svg to set of points connected by lines
"""

# IMPORTS
import os
# Third party imports
from PIL import Image  # pip install Pillow


# import pypotrace # https://pypi.org/project/pypotrace/ the installation sucks, worth it?

# Local application imports


def convert_img_to_black_and_white(img_url_old: str, img_url_new: str) -> str:
    """
    Converts image to black and white using PIL library

    :param img_url_old: path/name of image to convert
    :param img_url_new: path/name of new converted image
    :return: path/name of new converted image
    """
    # TODO: does Pillow support other formats than png?
    image_file = Image.open(img_url_old)  # open color image
    image_file = image_file.convert('1')  # convert image to black and white
    image_file.save(img_url_new)  # save converted image
    return img_url_new


def convert_img_to_svg():
    """
    convert to numpy array

    :return:
    """
    """
    How?
    #1 Pypotrace - the installation sucks
    https://stackoverflow.com/questions/56396804/converting-a-bmp-png-jpeg-to-an-svg-file-using-python
    
    #2 potrace, imagemagick installed using homebrew sucks
    https://eprev.org/2015/05/27/converting-png-to-svg/
    https://stackoverflow.com/questions/56696496/how-to-convert-jpg-or-png-image-to-svg-and-save-it
    
    #3 pixel2svg idk how to install - where to download zip file, is pixel by pixel conversion what I want?
    https://pypi.org/project/pixel2svg/
    """
    pass


def testing():
    convert_img_to_black_and_white(r"Resources\test_image_beans.png", r"Resources\converted_beans.png")

def svg_to_gcode():
    print(open('Resources/sample_code_icon.svg', 'r', encoding='utf-8').read())



svg_to_gcode()
