import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Exchange Rate Dashboard",
    page_icon="💱",
    layout="wide"
)

st.title("💱 Exchange Rate Dashboard")

# Load data
@st.cache_data(ttl=3600)
def load_data():
    url = "https://raw.githubusercontent.com/lealine2501/Currency-Dashboard-99x/main/data/currencies.json"
    df = pd.read_json(url)
    df["Date"] = pd.to_datetime(df["Date"], unit="ms")
    df["Freq"] = df["Freq"].str.strip()
    return df

df = load_data()

# --- Latest rates summary ---
st.subheader("Latest Rates")
latest = df[df["Latest"] == 1][["Quote_CUR", "Base_CUR", "Rate", "Date", "Source"]].copy()
latest = latest.sort_values("Quote_CUR")
st.dataframe(latest, use_container_width=True, hide_index=True)

st.divider()

# --- Historical chart ---
st.subheader("Historical Rate Chart")

col1, col2 = st.columns(2)

with col1:
    quote_options = sorted(df["Quote_CUR"].unique())
    quote = st.selectbox("Quote currency (you get this many...)", quote_options, index=quote_options.index("NOK") if "NOK" in quote_options else 0)

with col2:
    base_options = sorted(df[df["Quote_CUR"] == quote]["Base_CUR"].unique())
    base = st.selectbox("Base currency (...per 1 of this)", base_options)

filtered = df[(df["Quote_CUR"] == quote) & (df["Base_CUR"] == base)].sort_values("Date")

if not filtered.empty:
    st.line_chart(filtered.set_index("Date")["Rate"])
    st.caption(f"Showing {len(filtered)} data points for {base} → {quote}")
else:
    st.info("No data for this currency pair.")

st.divider()

# --- Raw data explorer ---
with st.expander("View raw data"):
    st.dataframe(df, use_container_width=True, hide_index=True)

st.caption("Data refreshed hourly from Azure SQL via GitHub Actions.")