import streamlit as st
from PIL import Image
import docx2txt
from PyPDF2 import PdfReader

@st.cache_data
def cargar_imagen(image_file):
  img = Image.open(image_file)
  return img

def leer_pdf(file):
  pdfReader = PdfReader(file)
  count = len(pdfReader.pages)
  todo_el_texto = ""
  
  for i in range(count):
    pagina = pdfReader.pages[i]
    todo_el_texto += pagina.extract_text()
    
  return todo_el_texto