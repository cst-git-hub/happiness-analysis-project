def shrink_df(df, value_col, icc_col=None, year=None):

    if year is not None and "year" in df.columns:
        df = df[df["year"] == year]

    # columns to keep
    cols = ["country"]

    if icc_col is not None:
        cols.append(icc_col)

    cols.append(value_col)

    df = df[cols]

    # remove rows without country code
    if icc_col is not None:
        df = df.dropna(subset=[icc_col])


    return df.reset_index(drop=True)