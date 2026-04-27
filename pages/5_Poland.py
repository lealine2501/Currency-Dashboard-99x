import streamlit as st
import pandas as pd
from utils import load_data, get_pair, get_cross_pair, plot_history, build_matrix

st.markdown("""
    <style>
    .main { background-color: #f8f9fb; }
    h1, h2, h3 { color: #1B3D6E; }
    </style>
""", unsafe_allow_html=True)

st.title("Poland")
st.markdown("Exchange rates relevant to 99x Poland operations.")
st.divider()

df = load_data()

usd_nok = get_pair(df, "NOK", "USD")
pln_nok = get_pair(df, "NOK", "PLN")
usd_pln = get_cross_pair(usd_nok, pln_nok)

# --- PLN/NOK graph ---
st.subheader("PLN / NOK")
st.plotly_chart(plot_history(pln_nok, "NOK", "PLN"), use_container_width=True)

st.divider()

# --- USD/PLN graph ---
st.subheader("USD / PLN")
st.plotly_chart(plot_history(usd_pln, "PLN", "USD"), use_container_width=True)

st.divider()

# --- Matrix ---
st.subheader("Rate Matrix — NOK (last 24 months)")
st.caption("B = end of month rate · M = monthly average rate")

matrix_pln = build_matrix(pln_nok, "NOK", "PLN", "PLN/NOK")
matrix_usd_pln = build_matrix(usd_pln, "PLN", "USD", "USD/PLN")

matrix = pd.concat([matrix_pln, matrix_usd_pln])
st.dataframe(
    matrix.style.format("{:.4f}"),
    use_container_width=True
)
