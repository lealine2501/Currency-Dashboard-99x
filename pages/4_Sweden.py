import streamlit as st
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

st.subheader("SEK / NOK")
st.plotly_chart(plot_history(sek_nok, "NOK", "SEK"), use_container_width=True)

st.divider()

st.subheader("Rate Matrix — NOK (last 24 months)")
st.caption("B = end of month rate · M = monthly average rate")

matrix = build_matrix(sek_nok, "NOK", "SEK", "SEK/NOK")
st.dataframe(
    matrix.style.format("{:.4f}"),
    use_container_width=True
)