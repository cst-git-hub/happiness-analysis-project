import pandas as pd
import requests
from io import StringIO

url = "https://ourworldindata.org/grapher/ti-corruption-perception-index.csv"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

csv_data = StringIO(response.text)

df = pd.read_csv(csv_data)

print(df.head())

df.to_csv("data/raw/corruption_raw.csv", index=False)

print("Corruption dataset saved.")