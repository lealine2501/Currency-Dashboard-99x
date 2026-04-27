import streamlit as st
import pandas as pd
from utils import load_data, get_pair, plot_history, build_matrix

st.set_page_config(page_title="Sweden — 99x", page_icon="🇸🇪", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f8f9fb; }
    h1, h2, h3 { color: #1B3D6E; }
    </style>
""", unsafe_allow_html=True)

st.title("Sweden")
st.markdown("Exchange rates relevant to 99x Sweden operations.")
st.divider()

df = load_data()
sek_nok = get_pair(df, "NOK", "SEK")

nok_sek = sek_nok[["Date", "Rate"]].copy()
nok_sek["Rate"] = 1 / nok_sek["Rate"]

# --- SEK/NOK graph ---
st.subheader("SEK / NOK")
st.plotly_chart(plot_history(sek_nok, "NOK", "SEK"), use_container_width=True)

st.divider()

# --- NOK/SEK graph ---
st.subheader("NOK / SEK")
st.plotly_chart(plot_history(nok_sek, "SEK", "NOK"), use_container_width=True)

st.divider()

st.subheader("Rate Matrix — NOK (last 24 months)")
st.caption("B = end of month rate · M = monthly average rate")

matrix_sek = build_matrix(sek_nok, "NOK", "SEK", "SEK/NOK")
matrix_nok = build_matrix(nok_sek, "SEK", "NOK", "NOK/SEK")

matrix = pd.concat([matrix_sek, matrix_nok])
st.dataframe(
    matrix.style.format("{:.4f}"),
    use_container_width=True
)
