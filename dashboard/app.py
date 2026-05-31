import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Sponge City Readiness Index",
    layout="wide"
)

# ----------------------------
# LOAD DATA
# ----------------------------

df = pd.read_csv(
    "scri_dashboard_data.csv"
)

# ----------------------------
# HEADER
# ----------------------------

st.title(
    "🌧 Sponge City Readiness Index (SCRI)"
)

st.markdown(
    """
    Climate Risk & Urban Resilience Analytics Platform
    """
)

# ----------------------------
# KPI CARDS
# ----------------------------

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Grid Cells",
    len(df)
)

col2.metric(
    "Average SCRI",
    round(df["scri"].mean(),1)
)

col3.metric(
    "Best SCRI",
    round(df["scri"].max(),1)
)

col4.metric(
    "Priority Zones",
    (df["scri_class"]=="Poor").sum()
)

# ----------------------------
# SCRI FILTER
# ----------------------------

scri_filter = st.sidebar.selectbox(

    "SCRI Class",

    [
        "All",
        "Poor",
        "Moderate",
        "Good",
        "Excellent"
    ]

)

if scri_filter == "All":
    filtered = df.copy()

else:

    filtered = df[
        df["scri_class"] == scri_filter
    ]

# ----------------------------
# INDIA MAP
# ----------------------------

st.subheader(
    "SCRI Spatial Distribution"
)

fig = px.scatter_map(

    filtered,

    lat="lat",
    lon="lon",

    color="scri",

    hover_data=[
        "scri",
        "mean_annual_rf",
        "dry_days",
        "heavy_days"
    ],

    zoom=4,

    height=700
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------
# SCRI CLASS BREAKDOWN
# ----------------------------

col1,col2 = st.columns(2)

with col1:

    fig = px.histogram(

        filtered,

        x="scri",

        nbins=30,

        title="SCRI Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    scri_counts = (

        filtered["scri_class"]

        .value_counts()

        .reset_index()

    )

    scri_counts.columns = [
        "SCRI Class",
        "Count"
    ]

    fig = px.bar(

        scri_counts,

        x="SCRI Class",

        y="Count",

        color="SCRI Class",

        title="SCRI Classes"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ----------------------------
# SCRI DRIVERS
# ----------------------------

st.subheader(
    "SCRI Components"
)

drivers = [

    "rainfall_score",

    "soil_score",

    "terrain_score",

    "water_norm",

    "permeability_norm",

    "vegetation_proxy"

]

driver_means = (

    filtered[drivers]

    .mean()

    .reset_index()

)

driver_means.columns = [

    "Factor",

    "Score"

]

fig = px.bar(

    driver_means,

    x="Factor",

    y="Score",

    color="Score",

    title="Average Sponge City Readiness Drivers"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------
# TOP PRIORITY ZONES
# ----------------------------

st.subheader(
    "Top 20 Priority Intervention Zones"
)

priority = filtered.nsmallest(
    20,
    "scri"
)

st.dataframe(

    priority[
        [
            "lat",
            "lon",
            "scri",
            "scri_class"
        ]
    ],

    use_container_width=True

)

# ----------------------------
# DOWNLOAD
# ----------------------------

csv = priority.to_csv(
    index=False
)

st.download_button(

    "Download Priority Zones",

    csv,

    file_name="priority_interventions.csv",

    mime="text/csv"

)

# ----------------------------
# FEATURE EXPLORER
# ----------------------------

st.subheader(
    "Feature Explorer"
)

feature = st.selectbox(

    "Select Feature",

    [

        "mean_annual_rf",

        "cv",

        "dry_days",

        "heavy_days",

        "soil_clay",

        "soil_soc",

        "slope",

        "water_occurrence"

    ]

)

fig = px.histogram(

    filtered,

    x=feature

)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------
# DATA TABLE
# ----------------------------

st.subheader(
    "SCRI Dataset"
)

st.dataframe(
    filtered
)