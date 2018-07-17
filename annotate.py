import argparse
from enum import Enum
import io
from PIL import Image as PilImage, ImageDraw
import json

# Google APIs
from google.cloud import vision
from google.cloud.vision import types

#from IPython.core.display import Image, display



client = vision.ImageAnnotatorClient()



def get_document_from_image(filein):
    """Sends the image to Google Vision API to get the annotations"""
    # Read image file
    #display(Image(image_file_name))
    with io.open(filein, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.document_text_detection(image=image)
    document = response.full_text_annotation
    return document

def get_document_from_url(url):
    """Sends the image to Google Vision API to get the annotations"""
    source = types.ImageSource(image_uri=url)
    image = types.Image(source=source)
    response = client.document_text_detection(image=image)
    document = response.full_text_annotation
    return document