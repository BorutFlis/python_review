import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(0)


def fill_within_year_merge_asof(df):
    column_names = df.columns
    combined_df = df.copy()
    for c in column_names:
        combined_df = pd.merge_asof(
            combined_df, combined_df[c].dropna(),
            tolerance=pd.Timedelta(days=365),  # only match if inside one year
            allow_exact_matches=False,  # don't match same rows
            left_index=True, right_index=True
        )
    result_df = (combined_df.iloc[:, :len(column_names)]
                 .set_axis(column_names, axis=1)
                 .combine_first(combined_df.iloc[:, len(column_names):].set_axis(column_names, axis=1))
                 )
    return result_df


def fill_within_year_resample(df):
    df = df.copy()

    daily_df = (
        df.resample("d")  # we oversampled our data-frame, so that we have an entry for each day
          .first().ffill(limit=365)  # we forward fill based on the last filled value being in the last 365 days
    )
    # select the days included in the original df
    df = daily_df.loc[df.index]
    return df


# Define a function to fill NaNs within one year of the last valid observation
def fill_within_year(df):
    # Create a copy of the DataFrame to not alter the original one
    df_filled = df.copy()

    # Loop over each column to apply the fill logic
    for column in df_filled.columns:
        # Forward fill with the condition of the time difference being less than or equal to one year
        for idx, value in df_filled[column].items():
            if pd.isna(value):
                # Get the most recent past value within one year
                past_values = df_filled[column][:idx].iloc[:-1]
                past_year_values = past_values[past_values.index >= (idx - pd.DateOffset(years=1))]
                if not past_year_values.empty:
                    df_filled.at[idx, column] = past_year_values.iloc[-1]

    return df_filled
