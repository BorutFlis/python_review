import pandas as pd
import numpy as np

df = pd.read_csv("test_data/uneven_intervals.csv")
df.columns = ["Datetime"] + df.columns.tolist()[1:]
df["Datetime"] = pd.to_datetime(df["Datetime"])
df = df.set_index("Datetime")

yearly_df = pd.read_csv("test_data/yearly.csv")
yearly_df.columns = ["Datetime", yearly_df.columns[1]]
yearly_df["Datetime"] = pd.to_datetime(yearly_df["Datetime"])
yearly_df = yearly_df.set_index("Datetime")

# task 1: merge df with yearly_df based on yearly difference
# task 2: write function to ffilna if difference less than one year

