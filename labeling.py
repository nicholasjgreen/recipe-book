import json
import re
import readchar
import os.path


def find_letter(letter, lst):
    return any(letter in word for word in lst)

def label_a_file(id):
    # Load the data files
    with open('extracted/data_{}.json'.format(id)) as extracted_text_file:
        extracted_text = json.load(extracted_text_file)
        extracted_text_file.close()

    # Which file is this?
    print('Labelling file: {}'.format(id))

    # Start a list of labels
    labels = []

    # Dump out the lines to the terminal
    for text_line in extracted_text:
        print(text_line)
        input_ok = False
        while not input_ok:
            print('(1) Recipe Name      (2) Description    (3) Ingredients    (4) Instructions     (5) Ignore    (q) Quit')
            ch = readchar.readchar()
            input_ok = find_letter(ch, [b'1', b'2', b'3', b'4', b'5', b'q'])
        # Stop if quit
        if ch == b'q':
            quit()
        # Add to list of labels
        labels.append(ord(ch) -48)
    print(labels)
    # Save it
    with open(labelled_file_name(id), 'w') as outfile:
        json.dump(labels, outfile)


def labelled_file_name(id):
    return 'extracted/labels_{}.json'.format(id)


# Load the list of images
with open('image_paths.json') as json_data:
    image_paths = json.load(json_data)
    json_data.close()
    images = image_paths["images"]

fileid_expr = re.compile('\/(.*)\.jpg$')

# Choose the first one
#imageUrl = images[0]

for imageUrl in images:
    id = fileid_expr.search(imageUrl).groups()[0]
    if not os.path.isfile(labelled_file_name(id)):
        label_a_file(id)
print('All done!')

