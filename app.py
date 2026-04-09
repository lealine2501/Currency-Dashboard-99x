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

col1, col2, col3, col4 = st.columns(4)

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

with col4:
    st.markdown("### 🇸🇪 Sweden")
    st.markdown("SEK / NOK")

st.divider()

df = load_data()

st.subheader("Latest Rates")
latest = df[df["Latest"] == 1].copy()
latest = latest[latest["Quote_CUR"] != latest["Base_CUR"]]
latest = latest[["Quote_CUR", "Base_CUR", "Rate", "Date", "Source"]]
latest["Date"] = latest["Date"].dt.strftime("%Y-%m-%d")
latest["Rate"] = latest["Rate"].round(4)
latest = latest