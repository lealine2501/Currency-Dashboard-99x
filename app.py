import streamlit as st

st.set_page_config(
    page_title="99x Currency Dashboard",
    page_icon="💱",
    layout="wide"
)

st.logo("99x_logo.jpg", size="large")

st.markdown("""
    <style>
    div[data-testid="stLogo"] {
        width: 100% !important;
        max-width: 100% !important;
    }
    div[data-testid="stLogo"] img {
        width: 100% !important;
        max-width: 100% !important;
        max-height: none !important;
    }
    </style>
""", unsafe_allow_html=True)

pg = st.navigation([
    st.Page("overview.py",          title="Overview",   icon="💱"),
    st.Page("pages/1_Brazil.py",    title="Brazil",     icon="🇧🇷"),
    st.Page("pages/2_Sri_Lanka.py", title="Sri Lanka",  icon="🇱🇰"),
    st.Page("pages/3_Portugal.py",  title="Portugal",   icon="🇵🇹"),
    st.Page("pages/4_Sweden.py",    title="Sweden",     icon="🇸🇪"),
    st.Page("pages/5_Poland.py",    title="Poland",     icon="🇵🇱"),
])
pg.run()
