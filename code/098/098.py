# Web API
import requests
import pandas as pd

station_id = "KSAC"
endpoint = f"https://api.weather.gov/stations/{station_id}/observations/latest"
data = requests.get(endpoint, timeout=10).json()
reading = data["properties"]

cols = ['elevation', 'temperature', 'dewpoint', 'windDirection',
    'windSpeed', 'windGust', 'barometricPressure', 'seaLevelPressure',
    'visibility', 'maxTemperatureLast24Hours', 'minTemperatureLast24Hours',
    'precipitationLastHour', 'precipitationLast3Hours', 'windChill',
    'precipitationLast6Hours', 'relativeHumidity', 'heatIndex']

data = {col: reading[col].get("value") for col in cols}
data['description'] = reading['textDescription']
df = pd.DataFrame([data])
for field, value in data.items():
    print(f"{field}: {value}")
    # elevation: 8
    # temperature: 14.4
    # dewpoint: 10
    # windDirection: 220
    # windSpeed: 9.36
    # windGust: None
    # barometricPressure: 101190
    # seaLevelPressure: 101170
    # visibility: 16090
    # maxTemperatureLast24Hours: None
    # minTemperatureLast24Hours: None
    # precipitationLastHour: None
    # precipitationLast3Hours: None
    # windChill: None
    # precipitationLast6Hours: None
    # relativeHumidity: 74.8764630203
    # heatIndex: None
    # description: Mostly Cloudy
