import pandas as pd
import streamlit as st
import plotly.graph_objects as go

GITHUB_URL = "https://raw.githubusercontent.com/lealine2501/Currency-Dashboard-99x/main/data/currencies.json"

@st.cache_data(ttl=3600)
def load_data():
    df = pd.read_json(GITHUB_URL)
    df["Date"] = pd.to_datetime(df["Date"], unit="ms")
    df["Freq"] = df["Freq"].str.strip()
    return df

def get_pair(df, quote, base):
    return df[
        (df["Quote_CUR"] == quote) & (df["Base_CUR"] == base)
    ].copy().sort_values("Date")

def to_monthly(pair_df, months):
    cutoff = pd.Timestamp.now() - pd.DateOffset(months=months)
    df = pair_df[pair_df["Date"] >= cutoff].copy()
    df["YearMonth"] = df["Date"].dt.to_period("M")
    monthly = df.groupby("YearMonth")["Rate"].mean().reset_index()
    monthly["YearMonth"] = monthly["YearMonth"].dt.to_timestamp()
    # Remove any future months
    monthly = monthly[monthly["YearMonth"] <= pd.Timestamp.now()]
    return monthly

def plot_history(pair_df, quote, base):
    monthly = to_monthly(pair_df, 24)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=monthly["YearMonth"],
        y=monthly["Rate"],
        mode="lines+markers",
        line=dict(color="#1B3D6E", width=2),
        marker=dict(size=5, color="#1B3D6E"),
        fill="tozeroy",
        fillcolor="rgba(27,61,110,0.07)"
    ))
    fig.update_layout(
        title=dict(text=f"{base} / {quote} — 2 year history", font=dict(size=14)),
        height=320,
        margin=dict(l=50, r=20, t=50, b=30),
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis=dict(showgrid=True, gridcolor="#f0f0f0", title="", dtick="M1", tickformat="%b %Y"),
        yaxis=dict(showgrid=True, gridcolor="#f0f0f0", title=f"{quote} per 1 {base}"),
        font=dict(family="Arial", size=11),
        showlegend=False
    )
    return fig

def plot_ltm(pair_df, quote, base):
    monthly = to_monthly(pair_df, 12)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=monthly["YearMonth"],
        y=monthly["Rate"],
        mode="lines+markers",
        line=dict(color="#1B3D6E", width=2),
        marker=dict(size=5, color="#1B3D6E"),
        fill="tozeroy",
        fillcolor="rgba(27,61,110,0.07)"
    ))
    fig.update_layout(
        title=dict(text=f"{base} / {quote} — LTM", font=dict(size=14)),
        height=320,
        margin=dict(l=50, r=20, t=50, b=30),
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis=dict(showgrid=True, gridcolor="#f0f0f0", title="", dtick="M1", tickformat="%b %Y"),
        yaxis=dict(showgrid=True, gridcolor="#f0f0f0", title=f"{quote} per 1 {base}"),
        font=dict(family="Arial", size=11),
        showlegend=False
    )
    return fig

def build_matrix(pair_df, quote, base, label):
    cutoff = pd.Timestamp.now() - pd.DateOffset(months=24)
    df = pair_df[pair_df["Date"] >= cutoff].copy()
    df["YearMonth"] = df["Date"].dt.to_period("M")
    eom = df.groupby("YearMonth")["Rate"].last()
    avg = df.groupby("YearMonth")["Rate"].mean()
    matrix = pd.DataFrame({
        f"{label} — EOM (B)": eom.round(4),
        f"{label} — Monthly avg (M)": avg.round(4)
    }).T
    matrix.columns = [str(c) for c in matrix.columns]
    return matrix