import requests
import pandas as pd

response = requests.get('https://api.weather.com/v1/location/{location}/data')
weather_data = response.json()
weather_df = pd.DataFrame(weather_data)



