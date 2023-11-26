import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import json


@st.cache_data
def load_data(url):
    data = pd.read_csv(url)
    return data

@st.cache_data
def load_geojson(url):
    with open(url) as response:
        countries = json.load(response)
    return countries

data_url = "data/archive/API_SP.DYN.TFRT.IN_DS2_en_csv_v2_5455118.csv"
geo_json_url = "data/countries.geojson"


def main():
    data = load_data(data_url)
    geojson = load_geojson(geo_json_url)

    st.title("Fertility Rates")
    st.markdown(
        """
        This app shows the fertility rates of different countries in the world.
        """
    )

    st.sidebar.title("Options")
    year = st.slider("Year", 1960, 2021, 2021)

    st.write("## Fertility Rates in", year)
    fig = go.Figure(
        go.Choroplethmapbox(
            geojson=geojson,
            locations=data["Country Code"],
            featureidkey="properties.ISO_A3",
            z=data[str(year)],
            colorscale="YlGn",
            zmin=0
        )
    )
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=1,
        mapbox_center={"lat": 32.732346, "lon": -117.196053},
        width=800,
        height=600,
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()