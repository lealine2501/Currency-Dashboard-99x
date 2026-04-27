import streamlit as st
import plotly.graph_objects as go
from utils import load_data

st.set_page_config(
    page_title="99x Currency Dashboard",
    page_icon="💱",
    layout="wide"
)

st.markdown("""
    <style>
    .main { background-color: #f8f9fb; }
    h1, h2, h3 { color: #1B3D6E; }
    div[data-testid="stPageLink"] a {
        display: block;
        padding: 1rem 1.25rem;
        background: white;
        border: 1px solid #e0e4ed;
        border-radius: 10px;
        text-decoration: none;
        transition: box-shadow 0.15s;
    }
    div[data-testid="stPageLink"] a:hover {
        box-shadow: 0 2px 10px rgba(27,61,110,0.12);
        border-color: #1B3D6E;
    }
    </style>
""", unsafe_allow_html=True)

st.title("99x Currency Dashboard")
st.markdown(
    "This dashboard tracks exchange rates relevant to 99x subsidiary operations across five countries. "
    "All rates are sourced from Norges Bank and refreshed hourly. "
    "Select a country below to view historical graphs and monthly rate matrices."
)

st.divider()

countries = {
    "Brazil":     {"iso": "BRA", "flag": "🇧🇷"},
    "Sri Lanka":  {"iso": "LKA", "flag": "🇱🇰"},
    "Portugal":   {"iso": "PRT", "flag": "🇵🇹"},
    "Sweden":     {"iso": "SWE", "flag": "🇸🇪"},
    "Poland":     {"iso": "POL", "flag": "🇵🇱"},
}

fig_map = go.Figure(go.Choropleth(
    locations=[c["iso"] for c in countries.values()],
    z=[1] * len(countries),
    text=[f"{c['flag']} {name}" for name, c in countries.items()],
    hovertemplate="%{text}<extra></extra>",
    colorscale=[[0, "#1B3D6E"], [1, "#1B3D6E"]],
    showscale=False,
    marker_line_color="white",
    marker_line_width=1.5,
))
fig_map.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        coastlinecolor="#d0d5e0",
        showland=True,
        landcolor="#f0f2f6",
        showocean=True,
        oceancolor="#e8eef7",
        showlakes=False,
        projection_type="natural earth",
    ),
    margin=dict(l=0, r=0, t=0, b=0),
    height=380,
    paper_bgcolor="#f8f9fb",
)
st.plotly_chart(fig_map, use_container_width=True)

st.subheader("Select a country")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.page_link("pages/1_Brazil.py", label="🇧🇷  Brazil", icon=None)
    st.caption("BRL / NOK · USD / BRL")

with col2:
    st.page_link("pages/2_Sri_Lanka.py", label="🇱🇰  Sri Lanka", icon=None)
    st.caption("LKR / NOK · USD / LKR")

with col3:
    st.page_link("pages/3_Portugal.py", label="🇵🇹  Portugal", icon=None)
    st.caption("EUR / NOK")

with col4:
    st.page_link("pages/4_Sweden.py", label="🇸🇪  Sweden", icon=None)
    st.caption("SEK / NOK · NOK / SEK")

with col5:
    st.page_link("pages/5_Poland.py", label="🇵🇱  Poland", icon=None)
    st.caption("PLN / NOK · USD / PLN")

st.divider()

st.subheader("Latest Rates")
df = load_data()
latest = df[df["Latest"] == 1].copy()
latest = latest[latest["Quote_CUR"] != latest["Base_CUR"]]
latest = latest[["Quote_CUR", "Base_CUR", "Rate", "Date", "Source"]]
latest["Date"] = latest["Date"].dt.strftime("%Y-%m-%d")
latest["Rate"] = latest["Rate"].round(4)
st.dataframe(latest, use_container_width=True, hide_index=True)
