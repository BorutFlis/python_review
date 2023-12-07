import pandas as pd
import numpy as np

df = pd.read_csv("test_data/england-premier-league-matches-2017-to-2018-stats.csv")
last_row = df.iloc[-1]

df_with_nans = df.loc[:, ["home_team_goal_count", "away_team_goal_count"]]
df_with_nans.iloc[np.random.randint(0, len(df), 100), 1] = np.nan
df_with_nans.iloc[np.random.randint(0, len(df), 100), 0] = np.nan

# task 1: make dummies out of team_name and then broadcast the home_team_goal_count to the dummy matrix
# task 2: fill na values in df_with_nans with mean of home/away goal count do it for both axes
# task 3: add last row to data-frame
# task 4: multiply each column with a different value