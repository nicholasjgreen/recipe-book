# Google APIs
from google.cloud.vision import types


def get_para_texts_from_doc(document):
    para_texts = []

    # Process each page
    for page in document.pages:
        # Process each block in the page
        for block in page.blocks:
            # Process each paragraph in the block
            for para in block.paragraphs:
                # Process each word in the paragraph
                para_text = ""
                for word in para.words:
                    # Process each symbol in the word
                    for symbol in word.symbols:
                        # Process the symbol
                        para_text += symbol.text

                        # Check for breaks
                        if symbol.property.detected_break.type == types.TextAnnotation.DetectedBreak.SPACE:
                            para_text += " "

                        if symbol.property.detected_break.type == types.TextAnnotation.DetectedBreak.SURE_SPACE:
                            para_text += " "

                        if symbol.property.detected_break.type == types.TextAnnotation.DetectedBreak.EOL_SURE_SPACE:
                            para_text += "\n"

                        if symbol.property.detected_break.type == types.TextAnnotation.DetectedBreak.LINE_BREAK:
                            para_text += "\n"
                            # display(symbol.property.detected_break)
                # Para finished
                para_texts.append((para_text))

    return para_texts