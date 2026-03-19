import pandas as pd
from pathlib import Path

from utils.rename_cols import rename_cols
from utils.shrink_df import shrink_df

# root project directory
BASE_DIR = Path(__file__).resolve().parents[1]

raw_file = BASE_DIR / "data" / "raw" / "democracy_raw.csv"
clean_file = BASE_DIR / "data" / "clean" / "democracy_cleaned.csv"


# load raw
df = pd.read_csv(raw_file)

# rename columns
df = rename_cols(
    df,
    country_col="REF_AREA_LABEL",
    icc_col="REF_AREA",
    year_col="TIME_PERIOD",
    value_col="OBS_VALUE",
    new_value_name="DI"
)

# shrink (2024)
df = shrink_df(df, "DI", "icc", 2024)

# save
df.to_csv(clean_file, index=False)

print("Democracy dataset cleaned.")
print(df.head())