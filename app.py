import streamlit as st
from utils import load_data

st.set_page_config(
    page_title="99x Currency Dashboard",
    page_icon="💱",
    layout="wide"
)

st.markdown("""
    <style>
    .main { background-color: #f8f9fb; }
    h1 { color: #1B3D6E; }
    h2 { color: #1B3D6E; }
    </style>
""", unsafe_allow_html=True)

st.title("99x Currency Dashboard")
st.markdown("Live exchange rate tracking for 99x subsidiaries. Data refreshes hourly.")

st.divider()

df = load_data()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🇧🇷 Brazil")
    st.markdown("USD / NOK")
    st.markdown("BRL / NOK")

with col2:
    st.markdown("### 🇱🇰 Sri Lanka")
    st.markdown("LKR / NOK")

with col3:
    st.markdown("### 🇵🇹 Portugal")
    st.markdown("EUR / NOK")

st.divider()

st.subheader("Latest Rates")
latest = df[df["Latest"] == 1][["Quote_CUR", "Base_CUR", "Rate", "Date", "Source"]].copy()
latest["Date"] = latest["Date"].dt.strftime("%Y-%m-%d")
latest["Rate"] = latest["Rate"].round(4)
latest = latest.sort_values("Quote_CUR")
st.dataframe(latest, use_container_width=True, hide_index=True)

st.caption("Data sourced from Azure SQL via GitHub Actions.")