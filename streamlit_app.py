import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ------------------------------------------------
# CONFIGURACIÓN
# ------------------------------------------------
st.set_page_config(
    page_title="ECOVIDA Dashboard",
    page_icon="🌱",
    layout="wide"
)

# ------------------------------------------------
# ESTILO
# ------------------------------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7f6;
}

h1, h2, h3 {
    color: #14532d;
}

[data-testid="metric-container"] {
    background-color: white;
    border-radius: 15px;
    padding: 15px;
    box-shadow: 0px 0px 8px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# DATOS SIMULADOS
# ------------------------------------------------
np.random.seed(42)

n = 150

forest_data = pd.DataFrame({
    "Predio": np.random.choice([
        "Horizontes",
        "Lomas de Dapa"
    ], n),

    "Especie": np.random.choice([
        "Cedro",
        "Nogal",
        "Guayacán",
        "Carbonero"
    ], n),

    "DAP": np.random.normal(12, 4, n),
    "Altura": np.random.normal(5, 2, n),
    "Biomasa": np.random.normal(30, 10, n),
    "Carbono": np.random.normal(14, 4, n),

    "Estado": np.random.choice([
        "Saludable",
        "Regular",
        "Crítico"
    ], n)
})

# ------------------------------------------------
# TÍTULO
# ------------------------------------------------
st.title("🌱 Plataforma de Restauración Ecológica")

st.subheader(
    "Corporación Ecovida — Horizontes y Lomas de Dapa"
)

st.markdown("---")

# ------------------------------------------------
# TÍTULO
# ------------------------------------------------
st.title("🌱 Plataforma de Restauración Ecológica")

st.subheader(
    "Corporación Ecovida — Horizontes y Lomas de Dapa"
)

st.markdown("---")

# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------
st.sidebar.title("🌍 Navegación")

predio = st.sidebar.selectbox(
    "Selecciona un predio",
    ["Todos", "Horizontes", "Lomas de Dapa"]
)

# ------------------------------------------------
# FILTRO
# ------------------------------------------------
if predio != "Todos":
    forest_data = forest_data[
        forest_data["Predio"] == predio
    ]

# ------------------------------------------------
# KPIs
# ------------------------------------------------
st.markdown("## 📊 Indicadores Generales")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🌳 Árboles",
        len(forest_data)
    )

with col2:
    st.metric(
        "📏 DAP promedio",
        f"{forest_data['DAP'].mean():.2f} cm"
    )

with col3:
    st.metric(
        "🌱 Biomasa total",
        f"{forest_data['Biomasa'].sum():.2f} kg"
    )

with col4:
    st.metric(
        "🌎 Carbono total",
        f"{forest_data['Carbono'].sum():.2f} kg"
    )

# ------------------------------------------------
# GRÁFICAS
# ------------------------------------------------
st.markdown("---")
st.markdown("## 📈 Análisis Visual")

col5, col6 = st.columns(2)

with col5:
    fig1 = px.histogram(
        forest_data,
        x="DAP",
        color="Predio",
        title="Distribución de DAP"
    )

    st.plotly_chart(fig1, use_container_width=True)

with col6:
    fig2 = px.box(
        forest_data,
        x="Especie",
        y="Biomasa",
        color="Especie",
        title="Biomasa por especie"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ------------------------------------------------
# ESTADO FITOSANITARIO
# ------------------------------------------------
st.markdown("---")
st.markdown("## 🩺 Estado Fitosanitario")

estado_data = (
    forest_data["Estado"]
    .value_counts()
    .reset_index()
)

estado_data.columns = [
    "Estado",
    "Cantidad"
]

fig3 = px.pie(
    estado_data,
    names="Estado",
    values="Cantidad",
    title="Estado fitosanitario"
)

st.plotly_chart(fig3, use_container_width=True)

# ------------------------------------------------
# TABLA
# ------------------------------------------------
st.markdown("---")
st.markdown("## 🌳 Registro de Individuos")

st.dataframe(
    forest_data,
    use_container_width=True
)

# ------------------------------------------------
# FORMULARIO
# ------------------------------------------------
st.markdown("---")
st.markdown("## ➕ Registrar nuevo individuo")

with st.form("registro"):

    especie = st.text_input("Especie")

    dap = st.number_input(
        "DAP (cm)",
        min_value=0.0
    )

    altura = st.number_input(
        "Altura (m)",
        min_value=0.0
    )

    biomasa = st.number_input(
        "Biomasa (kg)",
        min_value=0.0
    )

    estado = st.selectbox(
        "Estado fitosanitario",
        ["Saludable", "Regular", "Crítico"]
    )

    submit = st.form_submit_button(
        "Guardar registro"
    )

    if submit:
        st.success(
            "✅ Registro guardado correctamente"
        )

# ------------------------------------------------
# FOOTER
# ------------------------------------------------
st.markdown("---")

st.caption(
    "Proyecto de monitoreo ecológico y restauración forestal 🌱"
)
