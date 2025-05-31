import streamlit as st
import os
import nbformat
from nbconvert import HTMLExporter
import streamlit.components.v1 as components

st.set_page_config(page_title="📓 Galery", layout="wide")
st.title("Notebooks")

# Carpeta donde guardas tus notebooks
NOTEBOOK_DIR = "DL_ipynb"

# Obtener la lista de archivos .ipynb
notebooks = [f for f in os.listdir(NOTEBOOK_DIR) if f.endswith(".ipynb")]

# Sidebar
st.sidebar.title("Nav")
menu = st.sidebar.radio("Ir a:", ["📒 Notebooks", "👩‍💻 About Me"])

# Página de Notebooks
if menu == "📒 Notebooks":
    selected_notebook = st.sidebar.selectbox("Pick a notebook", notebooks)
    
    if selected_notebook:
        notebook_path = os.path.join(NOTEBOOK_DIR, selected_notebook)
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)

        # Convertir a HTML
        html_exporter = HTMLExporter()
        html_exporter.exclude_input = False  # Cambia a True si no quieres mostrar el código
        (body, _) = html_exporter.from_notebook_node(nb)

        # Mostrar en Streamlit
        components.html(body, height=800, scrolling=True)

# Página "About Me"
elif menu == "👩‍💻 About Me":
    st.subheader("👩‍💻 This project")
    st.markdown("""
    Hi, Im Hildegard Zerrweck 👋🏼

    Este proyecto es una galería interactiva de notebooks que he desarrollado como parte de mi aprendizaje en temas de inteligencia artificial y aprendizaje profundo.

    En esta app podrás explorar notebooks directamente desde el navegador, sin necesidad de abrir Jupyter.  
    Utilicé **Streamlit**, **nbconvert** y un poco de lógica en Python para convertir notebooks `.ipynb` en visualizaciones HTML incrustadas.

    ### Funcionalidades:
    - Visualización de notebooks de forma ordenada
    - Interfaz intuitiva y amigable
    - Exploración rápida desde el sidebar

    Gracias por visitar ✨
    """)

