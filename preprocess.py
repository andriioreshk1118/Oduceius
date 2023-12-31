import os
import pytesseract
from PIL import Image 
from pytesseract import pytesseract 
import pandas as pd
from pdf2image import convert_from_path
import pathlib 
from pathlib import Path

path_to_tesseract = r"C:/Program Files/Tesseract-OCR/tesseract.exe"


def load_pdf_list(dir_path):
  pdf_list = []
  entries = Path(dir_path)
  for entry in entries.iterdir():
    if pathlib.Path(entry).suffix == '.pdf':
       pdf_list.append(entry)
  return pdf_list

def convert_pdf2img(pdf_path):
   split_tup = os.path.splitext(pdf_path)
   file_name = split_tup[0]
   image_path = file_name + '.png'
   images = convert_from_path(pdf_path)
   images[0].save(image_path, 'png')


def get_all_img_files(img_dir_path):
    img_list =[]
    entries = Path(img_dir_path)
    for entry in entries.iterdir():
        if pathlib.Path(entry).suffix == '.png':
            img_list.append(entry)
    return img_list

