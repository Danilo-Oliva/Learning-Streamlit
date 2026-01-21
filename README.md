# Aprendiendo Streamlit

Este repositorio es mi espacio personal de práctica y documentación.

### 🎯 Objetivo
Mi meta es aprender a crear aplicaciones web con Python usando el framework **Streamlit**.

Iré subiendo aquí todo mi código, ejercicios y pruebas a medida que avance en mi aprendizaje, empezando desde cero.

## 📝 Notas de mi aprendizaje
>STREAMLIT NO NECESITA INSTALAR ALGUNAS LIBRERIAS COMO PANDAS, YA TRAE INCLUIDAS MUCHAS.

>Creo el repo, el redme y el venv.

>Instalamos streamlite

>Creamos una función main para poner todo lo relacionado a streamlit

>*st.title("titulo")* -> es un H1
>*st.header("encabezado")* -> es un H2
>*st.subheader("subencabezado)* -> es un H3
> *st.text("texto")* -> es un texto simple, ni siquiera es un p
> *st.text(f"texto {variable}")* -> funciona como un printf
>*st.markdown("###texto")* -> Los # sirven para bajar el nivel de h, tres # equivalen a un H3

>*st.success("Éxito")* -> Son mensajes formateados, en este caso abrá un div pintado de verde con el mensaje dentro
>*st.warning("Advertencia")* -> Este es verde
>*st.info("Esto es información")* -> Este es azul
>*st.error("Esto es un error")* -> Este es rojo
>*st.exception("Esto es una excepción")* -> Este es como un error pero para excepciones

>*st.write("texto")* -> Sirve para mostrar todo tipo de texto, en cambio el text es sin formato. Incluso sirve para mostrar dataframes

>*st.dataframe(nombre del df)* -> Sirve para mostrar dataframes.

>*st.dataframe(nombre_del_dataframe.style.higlight_max(axis=0))* -> Sirve para mostrar en amarillo los resultados maximos de una columna, pero para esto el df debe tener igual o menos a 262144 filas.

>*st.write(df.head(numero de filas que querramos mostrar))* -> Primeras filas de un dataframe.
>*st.json({"clave": "valor"})* -> Sirve para mostrar cosas en formato json (se parece a código).

>*codigo = """* 
>  *def saludar():*
>    *print("Hola")*
>    *"""*
>*set.code(codigo, languaje="python")* -> podemos mostrar código en formato código.

> *opcion = st.selectbox('texto a mostrar', ['item_1', 'item_2'])* -> sirve para crear una caja de selecciones.

>*opciones = st.multiselect()* -> es lo mismo que selectbox pero este podes elegir varios.

>*edad = st.slider('texto a mostrar', min_value=0, max_value=100, value=25, step=1)* -> Sirve para crear un slider como el del volumen, el value es el valor por defecto y el step sera cuanto avanzamos o retrocedemos por cada movimiento que hacemos.

>*nivel = st.select_slider('texto a mostrar', options=['opcion_1', 'opcion_2'], value='medio')* -> Esto sirve para el slider pero con textos.

># Para las imagenes vamos a importar *from PIL import Image*
>*img = Image.open("rute de la imagen.formato")*
>*st.image(img, use_column_width=True)* -> Muestra la imagen, el use_column_width sirve para usar el ancho completo de la columna

># Para los videos vamos a importar *with open("ruta del video", "rb") as video_file:*
>*st.video(video_file.read(), start_time=0)* -> con esto mostramos el video.

># Para las canciones es lo mismo *with open("ruta de la cancion", "rb") as audio_file:*
>*st.audio(audio_file.read())* -> Mostrará el audio.

>*nombre = st.text_input("texto a mostrar")* -> Sirve para que el usuario ingrese texto.

>*mensaje = st.text_area("texto a mostrar", height=100)* -> sirve para que el usuario ingrese el texto que quiera como un mensaje. El height sirve para que sea más grande el área de escritura.

>*numero = st.number_input("texto a mostrar", 1.0, 25.0, step=1.0)* -> Sirve para que el usuario ingrese numeros y se le asigna el valor minimo y maximo. El ultimo valor es el step para que aumente o disminuya. Para que no aparezca en decimales, le quitamos el punto.

>*fecha = st.date_input("texto a mostrar")* -> Selecciona una fecha.

>*hora = st.time_input("texto a mostrar")* -> Selecciona una hora y minutos.

>*color = st.color_picker("texto a mostrar")* -> Selecciona un color.

# Personalización
> *st.set_page_config(page_title="nombre que querramos")* -> Sirve para cambiarle el a la pestaña. Va antes de cualquier función.

> *st.set_page_config(page_icon="img")* -> Sirve para poner un icono personalizado en la pestaña. Para esto necesitamos importar from PIL import Image -> img = Image.open("logo.png")

>*st.set_page_config(layout="wide")* -> Hace que la página sea mas ancha.

>*st.sidebar.header/write("texto")* -> Sirve para tener una barra lateral desplegable.

>*st.set_page_config(initial_sidebar_state="collapsed")* -> Hace que la barra desplegable esté contraida cuando se carga la página.

>*st.sidebar.selectbox("nombre del menu", variable que contiene la lista con las opciones)* -> Sirve para agregar opciones a la sidebar
  menu = ["imagenes", "conjunto de datos", "archivos de documentos" ]
  eleccion = st.sidebar.selectbox("Menu", menu)

> Podemos usar if == eleccion para que se vaya cambiando de paginas

# Plotly
> Sirve para crear gráficos y esas cosas de estadística.
> Para usar esta libreria tenemos que instalarla con el pip install.
> A continuación voy a simplemente colocar el fragmento de código porque no soy de usar mucho esto. Antes que nada hay que importar pandas

  import plotly.express as px
  import pandas as pd

  df = pd.read_csv("nombre del csv)
  st.dataframe(df)

  df_count = df.groupby('Gender').count().reset_index() -> Nuevo df
  fig = px.pie(df_count, values="EmpID", names="Gender", title="Género") -> gráfico de torta, por eso "pie".

  st.plotly_chart(fig) -> mostramos

  df_avg = df.groupby('Dept')['Stress'].mean().reset_index()
  fig2 = px.bar(df_avg, x:"Dept", y:"Stress", color="Dept")

  st.plotly_chart(fig2)

# Carga de archivos
> Instalar libreria docx2txt y PyPDF2 (importar PdfReader)
> *@st.cache_data* -> Es un decorador que permite almacenar en cache las cosas así no deben cargar varias veces lo mismo.

> *PdfReader(file)* -> Nos permite leer pdf, para contar cuantas páginas tiene usamos count = len(pdfReader.pages)

def leer_pdf(file):
  pdfReader = PdfReader(file)
  count = len(pdfReader.pages)
  todo_el_texto = ""
  
  for i in range(count):
    pagina = pdfReader.pages[i]
    todo_el_texto += pagina.extract_text()
    
  return todo_el_texto

> Lo que se hace es que pdfReader obtiene cada paginas en una lista. Por eso se obtiene el tamaño de las paginas, en la primera iteracion se obtiene la primera página y asi sucesivamente. Luego se concatena todo en una misma variable. Luego concatena todo el texto de una página con la anterior.

> *archivo_imagen = st.file_uploader("texto a mostrar", type=["png", "jpg", "jpeg"])* -> Sirve para subir imagenes, al cargar no a a mostrar los detalles, por eso usaremos un diccionario
  detalles_archivo = {
    "nombre_archivo": archivo_imagen.name,
    "tipo_archivo": archivo_imagen.type,
    "tamaño_archivo": archivo_imagen.size
  }
> Para mostrar esto primero usamos este fragmento arriba de la creacion del diccionario 
  if archivo_imagen is not None:
    detalles_archivos = {...}

>*st.image(cargar_imagen(archivo_imagen), width=250)* -> sirve para mostrar la imagen como tal.

>*cargar csv o excel* -> Es lo mismo que imagenes, incluso el if is not none, solo cambia el type=["csv", "xlsx"]
>Para mostrar esto cambia un poco, primero para mostrar un archivo con coma(csv) hay que hacer:
  if detalles_archivo["tipo_archivo"] == "text/csv":
    df = pd.read_csv(archivo_datos)

>y para un xlsx es:
  elif detalles_archivo["tipo_archivo] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
    df = pd.read_excel(archivo_datos)

> al final ponemos *st.dataframe(df)* sin identar así lo hace cualquiera que sea su tipo de archivo pero para que no salte error, hacemos
  else:
    df = pd.DataFrame()

> *cargar documentos* -> se usa lo mismo, solo cambia el type=["pdf","docx", "txt"]. Además agregaremos un botón con *st.button("Procesar")*

>Para mostrar los documentos hacemos el if correspondiente y un *str(archivo_doc.read(), "utf-8")*
  if detalles_archivo["tipo_archivo"] == "text/plain":
    texto = str(archivo_doc.read(), "utf-8")
            
    st.write(texto)