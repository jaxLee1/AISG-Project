import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

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


color_scale = [[0, 'green'], [0.5, 'yellow'], [1, 'red']]

if activity == "Basketball Courts":
    df = pd.read_csv(".\data\\basketballCourts.csv")
    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude",
                       mapbox_style="carto-positron", zoom=11)
    st.plotly_chart(fig)
elif activity == "Bus Stops":
    df = pd.read_csv(".\data\\busStop.csv")
    df['color'] = np.random.uniform(0,1,5196)
    location = st.sidebar.selectbox(
    "Select which bus stop are you looking for",
    options=df['name']
    )
    if location is not None:
        if location == 'All':
            region = st.sidebar.selectbox(
                "Filter by Area",
                options=df['Area'].unique()
            )
            if region is not None:
                if region == None:
                    pass
                else:
                    df = df.query('Area==@region')
                    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", color="color", color_continuous_scale=color_scale, range_color = (0,1),
                       mapbox_style="carto-positron", zoom=11)
                    st.plotly_chart(fig)

        else:
            df = df.query('name==@location')
            fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", color="color", color_continuous_scale=color_scale, range_color = (0,1),
                       mapbox_style="carto-positron", zoom=11)
            st.plotly_chart(fig)


