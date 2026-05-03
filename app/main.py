import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Climate Dashboard", layout="wide")

st.title("🌍 Africa Climate Comparison Dashboard")

countries = ["ethiopia", "kenya", "nigeria", "sudan", "tanzania"]

dfs = []
for c in countries:
    try:
        df = pd.read_csv(f"data/{c}_clean.csv")
        df["Country"] = c.capitalize()
        dfs.append(df)
    except:
        st.warning(f"{c} data not found")

if len(dfs) == 0:
    st.error("No data files found in data/ folder")
else:
    df = pd.concat(dfs)

    selected = st.multiselect(
        "Select Countries",
        df["Country"].unique(),
        default=df["Country"].unique()
    )

    df = df[df["Country"].isin(selected)]

    st.subheader("🌡 Temperature Trend")
    fig1 = px.line(df, x="YEAR", y="T2M", color="Country")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("🌧 Precipitation Distribution")
    fig2 = px.box(df, x="Country", y="PRECTOTCORR")
    st.plotly_chart(fig2, use_container_width=True)