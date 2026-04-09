import streamlit as st
from utils import load_data, get_pair, plot_history, plot_ltm, build_matrix

st.set_page_config(page_title="Sri Lanka — 99x", page_icon="🇱🇰", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f8f9fb; }
    h1, h2, h3 { color: #1B3D6E; }
    </style>
""", unsafe_allow_html=True)

st.title("🇱🇰 Sri Lanka")
st.markdown("Exchange rates relevant to 99x Sri Lanka operations.")
st.divider()

df = load_data()
lkr_nok = get_pair(df, "NOK", "LKR")

st.subheader("LKR / NOK")
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(plot_history(lkr_nok, "NOK", "LKR"), use_container_width=True)
with col2:
    st.plotly_chart(plot_ltm(lkr_nok, "NOK", "LKR"), use_container_width=True)

st.divider()

st.subheader("Rate Matrix — NOK (last 24 months)")
st.caption("B = end of month rate · M = monthly average rate")

matrix = build_matrix(lkr_nok, "NOK", "LKR", "LKR/NOK")
st.dataframe(
    matrix.style.format("{:.4f}"),
    use_container_width=True
)