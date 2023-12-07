import json

import pandas as pd

stored_values = json.load(open("test_data/stored_values_multiple.json", "rt"))
markets = stored_values["result"]["markets"]

# task 1: create market level data-frame
# task 2: expand to selections level data-frame, ensure it has market level id and does not have column name confussion
# task 3: expand to value level data-frame
