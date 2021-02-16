


from dbnomics import fetch_series, fetch_series_by_api_link


df = fetch_series("AMECO/ZUTN/EA19.1.0.0.0.ZUTN")
print(df.head())
