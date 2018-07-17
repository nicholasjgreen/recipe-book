# Standard libraries
import json
import pprint
import re

# Shared code
from extract_tools import *
from doctools import *

# Google APIs
from google.cloud import vision

# create a client to talk with google apis
client = vision.ImageAnnotatorClient()

# Load the list of images
with open('image_paths.json') as json_data:
    image_paths = json.load(json_data)
    json_data.close()

images = image_paths["images"]
baseUrl = image_paths["baseUrl"]

# Prepare a regex for getting the file id
fileid_expr = re.compile('\/(.*)\.jpg$')

for imageUrl in images:
    # Get the id
    id = fileid_expr.search(imageUrl).groups()[0]

    # Create the document
    document = get_document_from_url(client, baseUrl + imageUrl)

    # Get the para text
    paras = get_para_texts_from_doc(document)
    print(paras)

    with open('data_{}.json'.format(id), 'w') as outfile:
        json.dump(paras, outfile)
