import streamlit as st
import pandas as pd
from utils import load_data, get_pair, get_cross_pair, plot_history, build_matrix

st.markdown("""
    <style>
    .main { background-color: #f8f9fb; }
    h1, h2, h3 { color: #C49FD5; }
    </style>
""", unsafe_allow_html=True)

st.title("Sri Lanka")
st.markdown("Exchange rates relevant to 99x Sri Lanka operations.")
st.divider()

df = load_data()

usd_nok = get_pair(df, "NOK", "USD")
lkr_nok = get_pair(df, "NOK", "LKR")
usd_lkr = get_cross_pair(usd_nok, lkr_nok)

# --- USD/NOK graphs ---
st.subheader("USD / NOK")
st.plotly_chart(plot_history(usd_nok, "NOK", "USD"), use_container_width=True)

st.divider()

# --- LKR/NOK graphs ---
st.subheader("LKR / NOK")
st.plotly_chart(plot_history(lkr_nok, "NOK", "LKR"), use_container_width=True)

st.divider()

# --- USD/LKR graphs ---
st.subheader("USD / LKR")
st.plotly_chart(plot_history(usd_lkr, "LKR", "USD"), use_container_width=True)

st.divider()

# --- Matrix ---
st.subheader("Rate Matrix — NOK (last 24 months)")
st.caption("B = end of month rate · M = monthly average rate")

matrix_usd = build_matrix(usd_nok, "NOK", "USD", "USD/NOK")
matrix_lkr = build_matrix(lkr_nok, "NOK", "LKR", "LKR/NOK")
matrix_usd_lkr = build_matrix(usd_lkr, "LKR", "USD", "USD/LKR")

matrix = pd.concat([matrix_usd, matrix_lkr, matrix_usd_lkr])
st.dataframe(
    matrix.style.format("{:.4f}"),
    use_container_width=True
)
