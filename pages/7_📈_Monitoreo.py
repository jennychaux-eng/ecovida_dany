import streamlit as st

st.title("📈 Monitoreo")

fecha = st.date_input(
    "Fecha de evaluación"
)

st.success(
    "Monitoreo registrado correctamente"
)
