def rename_cols(df, country_col, icc_col, year_col, value_col, new_value_name):
    rename_map = {
        country_col: "country",
        icc_col: "icc",
        value_col: new_value_name
    }
    if year_col:
        rename_map[year_col] = "year"

    df = df.rename(columns=rename_map)

    return df