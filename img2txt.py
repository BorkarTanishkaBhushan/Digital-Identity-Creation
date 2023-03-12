from pytesseract import pytesseract
from PIL import Image
import re
import os


path=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract(filename):

    try:
        pytesseract.tesseract_cmd=path

        text=pytesseract.image_to_string(filename)
        with open('file.txt','w') as f:

            f.write(text)




        return text

    except Exception as e:
        print(e)
        return 'Error'


result=extract('pancard.jpeg')
print(result)