import streamlit as st
from utils import load_data, get_pair, plot_history, build_matrix

st.markdown("""
    <style>
    .main { background-color: #f8f9fb; }
    h1, h2, h3 { color: #1B3D6E; }
    </style>
""", unsafe_allow_html=True)

st.title("Portugal")
st.markdown("Exchange rates relevant to 99x Portugal operations.")
st.divider()

df = load_data()
eur_nok = get_pair(df, "NOK", "EUR")

st.subheader("EUR / NOK")
st.plotly_chart(plot_history(eur_nok, "NOK", "EUR"), use_container_width=True)

st.divider()

st.subheader("Rate Matrix — NOK (last 24 months)")
st.caption("B = end of month rate · M = monthly average rate")

matrix = build_matrix(eur_nok, "NOK", "EUR", "EUR/NOK")
st.dataframe(
    matrix.style.format("{:.4f}"),
    use_container_width=True
)