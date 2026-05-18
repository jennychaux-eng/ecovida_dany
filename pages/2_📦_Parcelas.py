import streamlit as st
import pandas as pd

st.title("📦 Parcelas")

parcelas = pd.DataFrame({
    "Parcela": ["H1", "H2", "L1", "L2"],
    "Predio": [
        "Horizontes",
        "Horizontes",
        "Lomas",
        "Lomas"
    ],
    "Supervivencia": [88, 91, 86, 93]
})

st.dataframe(parcelas)
