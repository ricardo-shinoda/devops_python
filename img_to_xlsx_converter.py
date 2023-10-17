from PIL import Image
import pytesseract
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd
from unidecode import unidecode

image = Image.open('photo.jpeg')

text = pytesseract.image_to_string(image)


def clean_text(text):
    cleaned_text = unidecode(text)
    cleaned_text = ''.join(
        ['?' if ord(c) < 32 or ord(c) > 126 else c for c in cleaned_text])
    return unidecode(text)


cleaned_text = clean_text(text)

text_lines = text.split('\n')

df = pd.DataFrame(text_lines, columns=['Text'])

wb = Workbook()
ws = wb.active

for row in dataframe_to_rows(df, index=False, header=True):
    ws.append(row)

output_file = 'output.xlsx'
wb.save(output_file)

print(f'Image data saved to {output_file}')
