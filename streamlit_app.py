import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ------------------------------------------------
# CONFIGURACIÓN
# ------------------------------------------------
st.set_page_config(
    page_title="ECOVIDA",
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
    box-shadow: 0px 0px 10px rgba(0,0,0,0.05);
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# DATOS SIMULADOS
# ------------------------------------------------
np.random.seed(42)

n = 120

df = pd.DataFrame({

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
# SIDEBAR
# ------------------------------------------------
st.sidebar.title("🌍 Navegación")

predio = st.sidebar.selectbox(
    "Selecciona el predio",
    [
        "Horizontes",
        "Lomas de Dapa"
    ]
)

modulo = st.sidebar.selectbox(
    "Selecciona módulo",
    [
        "📊 Panel de Control",
        "📦 Parcelas",
        "🌳 Individuos",
        "📏 Dasometría",
        "🌱 Biomasa",
        "🌎 Carbono",
        "📈 Monitoreo"
    ]
)

# ------------------------------------------------
# HEADER
# ------------------------------------------------
st.title("🌱 Plataforma de Restauración Ecológica")

st.subheader(
    f"Corporación Ecovida — {predio}"
)

st.markdown("---")

# =================================================
# PANEL DE CONTROL
# =================================================
if modulo == "📊 Panel de Control":

    st.header("🖥️ Panel de Control")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Área", "12 ha")
    col2.metric("Supervivencia", "89%")
    col3.metric("Biomasa", "1.4 ton")
    col4.metric("Carbono", "0.7 ton")

    st.markdown("---")

    col5, col6 = st.columns(2)

    with col5:

        fig = px.histogram(
            df,
            x="DAP",
            title="Distribución DAP"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col6:

        fig2 = px.scatter(
            df,
            x="DAP",
            y="Altura",
            title="DAP vs Altura"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

# =================================================
# PARCELAS
# =================================================
elif modulo == "📦 Parcelas":

    st.header("📦 Parcelas")

    parcelas = pd.DataFrame({
        "Parcela": ["P1", "P2", "P3"],
        "Área": [400, 500, 600],
        "Supervivencia": [91, 84, 92]
    })

    st.dataframe(parcelas)

# =================================================
# INDIVIDUOS
# =================================================
elif modulo == "🌳 Individuos":

    st.header("🌳 Individuos")

    st.dataframe(df)

# =================================================
# DASOMETRÍA
# =================================================
elif modulo == "📏 Dasometría":

    st.header("📏 Dasometría")

    fig = px.box(
        df,
        y="DAP",
        title="Distribución DAP"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =================================================
# BIOMASA
# =================================================
elif modulo == "🌱 Biomasa":

    st.header("🌱 Biomasa")

    fig = px.histogram(
        df,
        x="Biomasa",
        title="Distribución Biomasa"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =================================================
# CARBONO
# =================================================
elif modulo == "🌎 Carbono":

    st.header("🌎 Carbono")

    st.metric(
        "Carbono almacenado",
        "1.6 ton"
    )

# =================================================
# MONITOREO
# =================================================
elif modulo == "📈 Monitoreo":

    st.header("📈 Monitoreo")

    estado = df["Estado"].value_counts()

    fig = px.pie(
        values=estado.values,
        names=estado.index,
        title="Estado fitosanitario"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
