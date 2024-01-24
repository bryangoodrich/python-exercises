import pandas as pd
import requests
import plotly.express as px

counties_url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
unemployment_url = "https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv"
df = pd.read_csv(unemployment_url, dtype={"fips": str, "unemp": float})
counties = requests.get(counties_url, timeout=10).json()

fig = px.choropleth(df, geojson=counties, 
    locations='fips', color='unemp',
    color_continuous_scale="Viridis",
    range_color=(0, 12), scope="usa",
    labels={'unemp':'unemployment rate'})
fig = fig.update_layout(
    margin={"r":0,"t":0,"l":0,"b":0}, 
    coloraxis_colorbar={"title": "% Unemployment"})
fig.write_image("map.png", width=1000, height=400)
