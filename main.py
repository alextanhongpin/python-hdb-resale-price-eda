import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import pyarrow

    return (pl,)


@app.cell
def _(pl):
    df = pl.read_csv(
        "data/Resale flat prices based on registration date from Jan-2017 onwards.csv",
        infer_schema_length=10000,
    )
    return (df,)


@app.cell
def _(df, pl):
    df_with_date = df.with_columns(
        pl.col("month").str.to_date(format="%Y-%m").alias("transacted_date"),
        (pl.col("floor_area_sqm") * 10.7639).round(0).alias("floor_area_sqft"),
    ).select(pl.exclude(["month"]))
    df_with_date.select(sorted(df_with_date.columns, reverse=False))
    return


if __name__ == "__main__":
    app.run()
