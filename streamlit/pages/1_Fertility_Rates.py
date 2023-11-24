import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

@st.cache_data
def load_data(url):
    data = pd.read_csv(url)
    return data

data_url = "data/archive/API_SP.DYN.TFRT.IN_DS2_en_csv_v2_5455118.csv"
geo_json_url = "data/countries.geojson"

def main():
    data = load_data(data_url)

    # Convert the '2018' column to numeric
    year = 2018
    year = st.slider("Year", 1960, 2021, 2021)
    filtered_data = data[["Country Code", str(year)]]
    st.write(filtered_data)

    m = folium.Map(location=[32.732346, -117.196053], zoom_start=2)
    folium.Choropleth(
        geo_data=geo_json_url,
        data=filtered_data,
        columns=["Country Code", str(year)],
        key_on="feature.properties.ISO_A3",  # Change this if necessary
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        nan_fill_color="black"  # Color for countries with no data
    ).add_to(m)

    folium_static(m)

if __name__ == "__main__":
    main()
