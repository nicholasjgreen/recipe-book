from PIL import Image as PilImage, ImageDraw


def get_document_bounds(document):
    symbol_bounds = []
    word_bounds = []
    para_bounds = []
    block_bounds = []
    page_bounds = []

    # Collect specified feature bounds by enumerating all document features
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    for symbol in word.symbols:
                        symbol_bounds.append(symbol.bounding_box)
                    word_bounds.append(word.bounding_box)
                para_bounds.append(paragraph.bounding_box)
            block_bounds.append(block.bounding_box)
        page_bounds.append(block.bounding_box)
    # The list `bounds` contains the coordinates of the bounding boxes.
    return symbol_bounds, word_bounds, para_bounds, block_bounds, page_bounds



def render_doc_text(filein_name, document):
    image = PilImage.open(filein_name)
    draw = draw_image(image)
    symbol_bounds, word_bounds, para_bounds, block_bounds, page_bounds = get_document_bounds(document)
    draw_boxes(draw, page_bounds, 'blue')
    draw_boxes(draw, block_bounds, 'red')
    draw_boxes(draw, para_bounds, 'yellow')
    return image


def draw_image(image):
    """Draws the image to be annotated"""
    return ImageDraw.Draw(image)


def draw_boxes(draw, bounds, color):
    """Draw a border around the image using the hints in the vector list."""

    for bound in bounds:
        draw.polygon([
            bound.vertices[0].x, bound.vertices[0].y,
            bound.vertices[1].x, bound.vertices[1].y,
            bound.vertices[2].x, bound.vertices[2].y,
            bound.vertices[3].x, bound.vertices[3].y], None, color)
    return draw

