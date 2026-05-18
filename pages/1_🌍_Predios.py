import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ------------------------------------------------
# CONFIG
# ------------------------------------------------
st.set_page_config(layout="wide")

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
# TÍTULO
# ------------------------------------------------
st.title("🌍 Predios")

st.markdown("""
Comparación ecológica entre:
- Horizontes (Bosque seco tropical)
- Lomas de Dapa (Bosque de niebla)
""")

# ------------------------------------------------
# TABS
# ------------------------------------------------
tab1, tab2 = st.tabs([
    "🌱 Horizontes",
    "🌿 Lomas de Dapa"
])

# =================================================
# HORIZONTES
# =================================================
with tab1:

    st.header("🌱 Horizontes")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Área", "12 ha")
    col2.metric("Supervivencia", "89%")
    col3.metric("Biomasa", "1.4 ton")
    col4.metric("Carbono", "0.7 ton")

    st.markdown("---")

    subt1, subt2, subt3, subt4 = st.tabs([
        "📦 Parcelas",
        "🌳 Individuos",
        "📏 Dasometría",
        "🌱 Biomasa"
    ])

    # ---------------------------------------------
    # PARCELAS
    # ---------------------------------------------
    with subt1:

        parcelas = pd.DataFrame({
            "Parcela": ["H1", "H2", "H3"],
            "Área": [400, 450, 500],
            "Supervivencia": [91, 84, 92]
        })

        st.dataframe(parcelas)

    # ---------------------------------------------
    # INDIVIDUOS
    # ---------------------------------------------
    with subt2:

        st.dataframe(df.head(20))

    # ---------------------------------------------
    # DASOMETRÍA
    # ---------------------------------------------
    with subt3:

        fig = px.histogram(
            df,
            x="DAP",
            title="Distribución DAP"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ---------------------------------------------
    # BIOMASA
    # ---------------------------------------------
    with subt4:

        fig2 = px.box(
            df,
            y="Biomasa",
            title="Biomasa"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

# =================================================
# LOMAS DE DAPA
# =================================================
with tab2:

    st.header("🌿 Lomas de Dapa")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Área", "18 ha")
    col2.metric("Supervivencia", "93%")
    col3.metric("Biomasa", "2.1 ton")
    col4.metric("Carbono", "1.1 ton")

    st.markdown("---")

    subt1, subt2, subt3, subt4 = st.tabs([
        "📦 Parcelas",
        "🌳 Individuos",
        "📏 Dasometría",
        "🌱 Biomasa"
    ])

    # ---------------------------------------------
    # PARCELAS
    # ---------------------------------------------
    with subt1:

        parcelas = pd.DataFrame({
            "Parcela": ["L1", "L2", "L3"],
            "Área": [600, 550, 700],
            "Supervivencia": [93, 95, 90]
        })

        st.dataframe(parcelas)

    # ---------------------------------------------
    # INDIVIDUOS
    # ---------------------------------------------
    with subt2:

        st.dataframe(df.tail(20))

    # ---------------------------------------------
    # DASOMETRÍA
    # ---------------------------------------------
    with subt3:

        fig = px.scatter(
            df,
            x="DAP",
            y="Altura",
            title="DAP vs Altura"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ---------------------------------------------
    # BIOMASA
    # ---------------------------------------------
    with subt4:

        fig2 = px.histogram(
            df,
            x="Biomasa",
            title="Distribución Biomasa"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )
