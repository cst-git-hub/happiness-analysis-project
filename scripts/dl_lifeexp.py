import pandas as pd
import requests
from io import StringIO

url_life = "https://www.worldometers.info/demographics/life-expectancy/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url_life, headers=headers)

html = response.text

tables = pd.read_html(StringIO(html))

life_df = tables[0]

print(life_df.columns)
print(life_df.head())

life_df.to_csv("data/raw/life_expectancy_raw.csv", index=False)

print("Life expectancy dataset saved.")