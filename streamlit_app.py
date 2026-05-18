import streamlit as st

# ------------------------------------------------
# CONFIG
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
# SIDEBAR
# ------------------------------------------------
st.sidebar.title("🌍 Navegación")

st.sidebar.success(
    "Plataforma de monitoreo ecológico"
)

# ------------------------------------------------
# HOME
# ------------------------------------------------
st.title("🌱 Plataforma de Restauración Ecológica")

st.subheader(
    "Corporación Ecovida — Horizontes y Lomas de Dapa"
)

st.markdown("---")

st.markdown("""
## Bienvenido

Esta plataforma permite:

- Monitorear especies arbóreas
- Analizar biomasa y carbono
- Evaluar restauración ecológica
- Visualizar métricas dasométricas
- Comparar predios restaurados
- Generar reportes técnicos
""")

st.image(
    "https://images.unsplash.com/photo-1441974231531-c6227db76b6e",
    use_container_width=True
)
