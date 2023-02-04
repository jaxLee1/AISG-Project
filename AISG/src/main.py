import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data
st.set_page_config(page_title="Allocation",
                    page_icon=":bar_chart:",
                    layout="wide")

st.sidebar.header("Filtering by Location")

## Selection of optimization function
activity = st.sidebar.selectbox(
    "Select Activities You Are Looking Forward To:",
    options=["Basketball Courts", "Bus Stops"]
)



if activity == "Basketball Courts":
    df = pd.read_csv(".\data\\basketballCourts.csv")
    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude",
                       mapbox_style="carto-positron", zoom=11)
    st.plotly_chart(fig)
elif activity == "Bus Stops":
    df = pd.read_csv(".\data\\busStop.csv")

    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude",
                       mapbox_style="carto-positron", zoom=11)
    st.plotly_chart(fig)



##color_scale = [[0, 'green'], [0.5, 'yellow'], [1, 'red']]

##fig = px.scatter_mapbox(df, lat="tip", lon="total_bill", color="sex", color_continuous_scale=color_scale,
##                       size="size", size_max=15, zoom=10)