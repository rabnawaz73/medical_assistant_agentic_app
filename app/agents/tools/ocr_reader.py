import easyocr

reader = easyocr.Reader(['en'])

def text_from_image(file_path):
    result = reader.readtext(file_path, detail=0)
    return ' '.join(result)