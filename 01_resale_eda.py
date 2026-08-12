import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl

    return (pl,)


@app.cell
def _(pl):
    df = pl.read_csv('data/Resale flat prices based on registration date from Jan-2017 onwards.csv', infer_schema_length=10000)
    df
    return (df,)


@app.cell
def _(df, pl):
    df_with_date = df.with_columns(
        pl.col("month").str.to_date(format='%Y-%m').alias("yyyy-mm")
    )
    df_with_date
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
