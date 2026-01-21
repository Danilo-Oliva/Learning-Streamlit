import streamlit as st
from cargar_archivos import cargar_imagen, leer_pdf
import pandas as pd
import docx2txt

st.set_page_config(page_title="Hola")


def main():
    st.title("Curso de Streamlit")
    nombre = st.text_input("Ingrese su nombre")

    st.header(f"Bienvenido {nombre}")

    menu = ["Imagenes", "Conjunto de Datos", "Archivos de Documentos"]
    eleccion = st.sidebar.selectbox("Menú", menu)

    if eleccion == "Imagenes":
      
        st.subheader(f"Bienvenido {nombre} a la carga de imagenes")
        archivo_imagen = st.file_uploader("Subir imagenes", type=["png", "jpg", "jpeg"])

        if archivo_imagen is not None:
          detalles_archivo = {
                "nombre_archivo": archivo_imagen.name,
                "tipo_archivo": archivo_imagen.type,
                "tamaño_archivo": archivo_imagen.size,
            }
          st.write(detalles_archivo)
          st.image(cargar_imagen(archivo_imagen), width=250)
    
    elif eleccion == "Conjunto de Datos":
      
      st.subheader(f"Bienvenido {nombre} a la carga de Conjunto de Datos")
      archivo_datos = st.file_uploader("Subir CSV o Excel", type=["csv", "xlsx"])
      
      if archivo_datos is not None:
        detalles_archivo = {
          "nombre_archivo": archivo_datos.name,
          "tipo_archivo": archivo_datos.type,
          "tamaño_archivo": archivo_datos.size
        }
        st.write(detalles_archivo)
        
        if detalles_archivo["tipo_archivo"] == "text/csv":
          df = pd.read_csv(archivo_datos)
        elif detalles_archivo["tipo_archivo"] == "application/vnd openxmlformats-officedocument.spreadsheetml.sheet":
          df = pd.read_excel(archivo_datos)
        else:
          df = pd.DataFrame()
          
        st.dataframe(df)
        
    elif eleccion == "Archivos de Documentos":
      st.subheader(f"Bienvenido {nombre} a la carga de Archivos de Documentos")
      
      archivo_doc = st.file_uploader("Subir Documento", type=["pdf", "docx", "txt"])
      
      if st.button("Procesar"):
        if archivo_doc is not None:
          detalles_archivo = {
            "nombre_archivo": archivo_doc.name,
            "tipo_archivo": archivo_doc.type,
            "tamaño_archivo": archivo_doc.size
          }
          st.write(detalles_archivo)
          
          if detalles_archivo["tipo_archivo"] == "text/plain":
            texto = str(archivo_doc.read(), "utf-8")
            st.write(texto)
            
          elif detalles_archivo["tipo_archivo"] == "application/pdf":
            texto = leer_pdf(archivo_doc)
            st.write(texto)
            
          elif detalles_archivo["tipo_archivo"] == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            texto = docx2txt.process(archivo_doc)
            st.write(texto)

if __name__ == "__main__":
    main()
