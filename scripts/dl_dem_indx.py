import requests
import pandas as pd
from io import StringIO

url = "https://data360files.worldbank.org/data360-data/data/EIU_DI/EIU_DI.csv"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

csv_data = StringIO(response.text)

df = pd.read_csv(csv_data)

print(df.head())
print(df.columns)

df.to_csv("data/raw/democracy_raw.csv", index=False)

print("Democracy dataset saved.")