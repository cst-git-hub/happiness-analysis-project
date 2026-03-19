import requests
import pandas as pd
from io import StringIO

url = "https://ourworldindata.org/grapher/happiness-cantril-ladder.csv"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

csv_data = StringIO(response.text)

df = pd.read_csv(csv_data)

print(df.columns.tolist())

df.to_csv("data/raw/happiness_raw.csv", index=False)

print("Happiness dataset saved.")