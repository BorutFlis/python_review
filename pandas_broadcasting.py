import pandas as pd
import numpy as np

df = pd.read_csv("test_data/england-premier-league-matches-2017-to-2018-stats.csv")
last_row = df.iloc[-1]

df_with_nans = df.loc[:, ["home_team_goal_count", "away_team_goal_count"]]
df_with_nans.iloc[np.random.randint(0, len(df), 100), 1] = np.nan
df_with_nans.iloc[np.random.randint(0, len(df), 100), 0] = np.nan

df1 = df[["home_team_goal_count", "home_team_shots"]]
df2 = df[["away_team_goal_count", "away_team_shots"]]
df_multi = pd.concat([
    df1.set_axis(pd.MultiIndex.from_tuples([("h", c) for c in df1.columns]), axis=1),
    df2.set_axis(pd.MultiIndex.from_tuples([("a", c) for c in df2.columns]), axis=1)
], axis=1)
multipliers = {"h":1, "a":22}

# task 1a: make dummies out of team_name and then broadcast the home_team_goal_count to the dummy matrix
#      1b: try to do 1a with pivot
#      1c: get series with first non-na for each column
#      1d: reverse get dummies operation
# task 2: fill na values in df_with_nans with mean of home/away goal count do it for both axes
# task 3: add last row to data-frame
# task 4a: multiply each column with a different value
# task 4b: multiply df_multi based on top-level and multipliers dict
