import streamlit as st

def main():
  st.title("Curso de Streamlit")
  nombre = st.text_input("Ingrese su nombre")
  
  st.header(f"Bienvenido {nombre}")
  
  mensaje = st.text_area("Escriba un mensaje", height=300)
  st.write(mensaje)
  
if __name__ == "__main__":
  main()