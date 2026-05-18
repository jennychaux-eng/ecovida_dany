import streamlit as st

st.title("🌳 Individuos Arbóreos")

codigo = st.text_input("Código del árbol")
especie = st.text_input("Especie")

st.file_uploader(
    "Subir fotografía",
    type=["png", "jpg", "jpeg"]
)

st.text_area("Observaciones")

st.button("Guardar")
