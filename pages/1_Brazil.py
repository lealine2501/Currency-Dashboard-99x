import streamlit as st
import pandas as pd
from utils import load_data, get_pair, get_cross_pair, plot_history, build_matrix

st.markdown("""
    <style>
    .main { background-color: #f8f9fb; }
    h1, h2, h3 { color: #C49FD5; }
    </style>
""", unsafe_allow_html=True)

st.title("Brazil")
st.markdown("Exchange rates relevant to 99x Brazil operations.")
st.divider()

df = load_data()

usd_nok = get_pair(df, "NOK", "USD")
brl_nok = get_pair(df, "NOK", "BRL")
usd_brl = get_cross_pair(usd_nok, brl_nok)

# --- USD/NOK graphs ---
st.subheader("USD / NOK")
st.plotly_chart(plot_history(usd_nok, "NOK", "USD"), use_container_width=True)

st.divider()

# --- BRL/NOK graphs ---
st.subheader("BRL / NOK")
st.plotly_chart(plot_history(brl_nok, "NOK", "BRL"), use_container_width=True)

st.divider()

# --- USD/BRL graphs ---
st.subheader("USD / BRL")
st.plotly_chart(plot_history(usd_brl, "BRL", "USD"), use_container_width=True)

st.divider()

# --- Matrix ---
st.subheader("Rate Matrix — NOK (last 24 months)")
st.caption("B = end of month rate · M = monthly average rate")

matrix_usd = build_matrix(usd_nok, "NOK", "USD", "USD/NOK")
matrix_brl = build_matrix(brl_nok, "NOK", "BRL", "BRL/NOK")
matrix_usd_brl = build_matrix(usd_brl, "BRL", "USD", "USD/BRL")

matrix = pd.concat([matrix_usd, matrix_brl, matrix_usd_brl])
st.dataframe(
    matrix.style.format("{:.4f}"),
    use_container_width=True
)