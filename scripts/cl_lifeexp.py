import pandas as pd
from pathlib import Path

from Happiness_analysis.utils.rename_cols import rename_cols
from Happiness_analysis.utils.shrink_df import shrink_df
from Happiness_analysis.utils.get_iso3 import get_iso3
#from Happiness_analysis.utils.fuzzmatching import suggest_country
from Happiness_analysis.utils.country_replace_map import country_fix

# root project directory
BASE_DIR = Path(__file__).resolve().parents[1]

raw_file = BASE_DIR / "data" / "raw" / "life_expectancy_raw.csv"
clean_file = BASE_DIR / "data" / "clean" / "life_expectancy_cleaned.csv"


# load raw
df = pd.read_csv(raw_file)

# rename columns
df = rename_cols(
    df,
    country_col="Country",
    icc_col=None,
    year_col=None,
    value_col="Life Expectancy (both sexes)",
    new_value_name="LE (ys)"
)

# shrink (2024)
df = shrink_df(df, "LE (ys)", None, None)

# replace country names with iso (pycountry) names
df["country"] = df["country"].replace(country_fix)

# add ISO3 country code
df["icc"] = df["country"].apply(get_iso3)

df = df.dropna(subset=["icc"])

# reorder columns
df = df[["country", "icc", "LE (ys)"]]

df.to_csv(clean_file, index=False)

print("Life expectancy dataset cleaned.")
print(df.head())