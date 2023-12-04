import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import json
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_prepare_data(fertility_data, gdp_data):
    # Reshape the datasets to long format
    fertility_long = fertility_data.melt(id_vars=['Country'], var_name='Year', value_name='Fertility Rate')
    gdp_long = gdp_data.melt(id_vars=['Country'], var_name='Year', value_name='GDP Per Capita')

    # Merge datasets on Country and Year
    merged_data = pd.merge(fertility_long, gdp_long, on=['Country', 'Year'])
    return merged_data

def plot_data(merged_data):
    # Calculate correlation
    correlation = merged_data[['Fertility Rate', 'GDP Per Capita']].corr()
    st.write("Correlation coefficient:", correlation.iloc[0, 1])

    # Scatter plot
    fig, ax = plt.subplots()
    sns.scatterplot(data=merged_data, x='Fertility Rate', y='GDP Per Capita', ax=ax)
    ax.set_title('Fertility Rate vs GDP Per Capita')
    st.pyplot(fig)

@st.cache_data
def load_data(url):
    data = pd.read_csv(url)
    return data

@st.cache_data
def load_geojson(url):
    with open(url) as response:
        countries = json.load(response)
    return countries

fert_url = "fertility_rate_pivot.csv"
gdp_url = "gdp_per_capita_pivot.csv"
geo_json_url = "data/countries.geojson"


def main():
    data_fert = load_data(fert_url)
    data_gdp = load_data(gdp_url)
    geojson = load_geojson(geo_json_url)

    st.title("Fertility Rates and GDP per Capita")
    st.markdown(
        """
        This app shows the fertility rates and GDP per capita of different countries in the world.
        """
    )

    if st.toggle("Show Analysis"):
        st.markdown(
            """
            ## Data Analysis: Fertility Rate vs GDP Per Capita
            """
        )
        merged_data = load_and_prepare_data(data_fert, data_gdp)
        plot_data(merged_data)

    year = st.slider("Year", 1960, 2015, 2015)



    
    st.write("## Fertility Rates in", year)
    fig = go.Figure(
        go.Choroplethmapbox(
            geojson=geojson,
            locations=data_fert["Country"],
            featureidkey="properties.ADMIN",
            z=data_fert[str(year)],
            colorscale="YlGn"
        )
    )
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=1,
        mapbox_center={"lat": 32.732346, "lon": -117.196053},
        width=800,  # Adjusted for column width
        height=600,
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig)

    
    st.write("## GDP per Capita in", year)
    fig2 = go.Figure(
        go.Choroplethmapbox(
            geojson=geojson,
            locations=data_gdp["Country"],
            featureidkey="properties.ADMIN",
            z=data_gdp[str(year)],
            colorscale="YlGn",
        )
    )
    fig2.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=1,
        mapbox_center={"lat": 32.732346, "lon": -117.196053},
        width=800,  # Adjusted for column width
        height=600,
    )
    fig2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig2)

if __name__ == "__main__":
    main()