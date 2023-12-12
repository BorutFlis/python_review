import pandas as pd
import numpy as np

groups = ["a", "b"]

df = pd.read_csv("test_data/uneven_intervals.csv")
df.columns = ["Datetime"] + df.columns.tolist()[1:]
df["Datetime"] = pd.to_datetime(df["Datetime"])
df = df.set_index("Datetime")
df["group"] = [groups[np.random.randint(len(groups))] for i in range(len(df))]

yearly_df = pd.read_csv("test_data/yearly.csv")
yearly_df.columns = ["Datetime", yearly_df.columns[1]]
yearly_df["Datetime"] = pd.to_datetime(yearly_df["Datetime"])
yearly_df = yearly_df.set_index("Datetime")
yearly_df["group"] = [groups[np.random.randint(len(groups))] for i in range(len(yearly_df))]


# task 1a: merge df with yearly_df based on yearly difference
# task 1b: merge df with yearly_df that merges on group before
# task 2: write function to ffilna if difference less than one year

