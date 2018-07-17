# Google APIs
from google.cloud import vision
from google.cloud.vision import types

# Standard apis
import io

def get_document_from_url(client, url):
    """Sends the image to Google Vision API to get the annotations"""
    source = types.ImageSource(image_uri=url)
    image = types.Image(source=source)
    response = client.document_text_detection(image=image)
    document = response.full_text_annotation
    return document

def get_document_from_image(client, image_file_name):
    """Sends the image to Google Vision API to get the annotations"""
    # Read image file
    #display(Image(image_file_name))
    with io.open(image_file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.document_text_detection(image=image)
    document = response.full_text_annotation
    return document
