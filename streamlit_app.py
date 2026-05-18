import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# ---------------------------------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------------------------------
st.set_page_config(
    page_title="Ecovida Dashboard",
    page_icon="🌱",
    layout="wide"
)

# ---------------------------------------------------
# ESTILO
# ---------------------------------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7f6;
}

h1, h2, h3 {
    color: #14532d;
}

.metric-card {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TÍTULO
# ---------------------------------------------------
st.title("🌱 Dashboard de Restauración Ecológica")
st.subheader("Corporación Ecovida - Horizontes y Lomas de Dapa")

st.markdown("""
Sistema de monitoreo del crecimiento y desempeño de especies arbóreas
en áreas restauradas del Valle del Cauca.
""")

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("⚙️ Panel de navegación")

predio = st.sidebar.selectbox(
    "Selecciona el predio",
    ["Todos", "Horizontes", "Lomas de Dapa"]
)

# ---------------------------------------------------
# DATOS SIMULADOS
# ---------------------------------------------------
np.random.seed(42)

n = 100

data = pd.DataFrame({
    "Predio": np.random.choice(["Horizontes", "Lomas de Dapa"], n),
    "Especie": np.random.choice(
        ["Cedro", "Guayacán", "Nogal", "Carbonero"],
        n
    ),
    "DAP": np.random.normal(12, 4, n),
    "Altura": np.random.normal(5, 2, n),
    "Biomasa": np.random.normal(35, 10, n),
    "Carbono": np.random.normal(16, 4, n),
    "Estado": np.random.choice(
        ["Saludable", "Regular", "Crítico"],
        n
    )
})

# FILTRO
if predio != "Todos":
    data = data[data["Predio"] == predio]

# ---------------------------------------------------
# KPIs
# ---------------------------------------------------
st.markdown("## 📊 Indicadores Generales")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🌳 Árboles monitoreados",
        len(data)
    )

with col2:
    st.metric(
        "📏 DAP promedio",
        f"{data['DAP'].mean():.2f} cm"
    )

with col3:
    st.metric(
        "🌿 Biomasa total",
        f"{data['Biomasa'].sum():.2f} kg"
    )

with col4:
    st.metric(
        "🌎 Carbono almacenado",
        f"{data['Carbono'].sum():.2f} kg"
    )

# ---------------------------------------------------
# GRÁFICAS
# ---------------------------------------------------
st.markdown("## 📈 Visualización de Datos")

col5, col6 = st.columns(2)

with col5:
    fig1 = px.histogram(
        data,
        x="DAP",
        nbins=20,
        title="Distribución de DAP"
    )

    st.plotly_chart(fig1, use_container_width=True)

with col6:
    fig2 = px.box(
        data,
        x="Especie",
        y="Biomasa",
        color="Especie",
        title="Biomasa por especie"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------
# ESTADO FITOSANITARIO
# ---------------------------------------------------
st.markdown("## 🩺 Estado Fitosanitario")

estado_count = data["Estado"].value_counts().reset_index()
estado_count.columns = ["Estado", "Cantidad"]

fig3 = px.pie(
    estado_count,
    names="Estado",
    values="Cantidad",
    title="Estado fitosanitario"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------------------------------------------
# TABLA DE DATOS
# ---------------------------------------------------
st.markdown("## 🗂️ Registro de individuos")

st.dataframe(data, use_container_width=True)

# ---------------------------------------------------
# FORMULARIO DE REGISTRO
# ---------------------------------------------------
st.markdown("## ➕ Registrar nuevo árbol")

with st.form("registro_arbol"):

    especie = st.text_input("Especie")
    dap = st.number_input("DAP (cm)", min_value=0.0)
    altura = st.number_input("Altura (m)", min_value=0.0)
    biomasa = st.number_input("Biomasa (kg)", min_value=0.0)

    submit = st.form_submit_button("Guardar registro")

    if submit:
        st.success("✅ Registro guardado correctamente")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")
st.caption("Proyecto de restauración ecológica - Ingeniería Ambiental 🌱")
