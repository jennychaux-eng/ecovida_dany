import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
st.title("📏 Dasometría")

n = 100

df = pd.DataFrame({
    "DAP": np.random.normal(12, 3, n),
    "Altura": np.random.normal(5, 1, n)
})

fig = px.scatter(
    df,
    x="DAP",
    y="Altura",
    title="DAP vs Altura"
)

st.plotly_chart(fig, use_container_width=True)
