import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))


import pandas as pd
#from pathlib import Path

from utils.rename_cols import rename_cols
from utils.shrink_df import shrink_df

# root project directory
BASE_DIR = Path(__file__).resolve().parents[1]

raw_file = BASE_DIR / "data" / "raw" / "corruption_raw.csv"
clean_file = BASE_DIR / "data" / "clean" / "corruption_cleaned.csv"


# load raw
df = pd.read_csv(raw_file)

# rename columns
df = rename_cols(
    df,
    country_col="Entity",
    icc_col="Code",
    year_col="Year",
    value_col="Corruption Perceptions Index",
    new_value_name="CPI"
)

# shrink (2024)
df = shrink_df(df, "CPI", "icc", 2024)

# save
df.to_csv(clean_file, index=False)

print("Corruption dataset cleaned.")
print(df.head())