import argparse
from enum import Enum
import io
from PIL import Image as PilImage, ImageDraw
import json

# Google APIs
from google.cloud import vision
from google.cloud.vision import types

#from IPython.core.display import Image, display


# Some config
#image_file_name = "cajun-potato-salad.jpg"
image_file_name = "cauliflower-soup.jpg"

class FeatureType(Enum):
    PAGE = 1
    BLOCK = 2
    PARA = 3
    WORD = 4
    SYMBOL = 5

client = vision.ImageAnnotatorClient()



def get_document_from_image(filein):
    """Sends the image to Google Vision API to get the annotations"""
    image = types.Image(content=content)
    response = client.document_text_detection(image=image)
    document = response.full_text_annotation
    return document

