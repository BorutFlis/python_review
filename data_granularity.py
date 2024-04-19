import json
import re

import pandas as pd

stored_values = json.load(open("test_data/stored_values_multiple.json", "rt"))
markets = stored_values["result"]["markets"]

shifts_df = pd.read_csv("test_data/2023020549.csv")


def add_constructor(period):
    def add(match_obj):
        return str(int(match_obj.group()) + (period - 1) * 20)

    return add


shifts_df["endTime"] = shifts_df.apply(lambda x: re.sub("^(\d{2})", add_constructor(x["period"]), x["endTime"]), axis=1)
shifts_df["startTime"] = shifts_df.apply(lambda x: re.sub("^(\d{2})", add_constructor(x["period"]), x["startTime"]), axis=1)


# task 1: create market level data-frame
# task 2: expand to selections level data-frame, ensure it has market level id and does not have column name confussion
# task 3: expand to value level data-frame
# task 4: change back to initial market-level granularity
# task 5: expand endTime - startTime
