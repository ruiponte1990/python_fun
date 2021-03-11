import sys
import pandas as pd
import json

if __name__ == "__main__":
    input_ = sys.argv[1]
    df = pd.read_csv(input_)
    cnt = 0
    out = {
        "user_list":[]
    }
    for index, row in df.iterrows():
        split = row['full_name'].split(" ")
        row_ = {
            "list_id": index+1,
            "first name": split[0],
            "last name": split[1],
            "email": row['email']
        }
        out["user_list"].append(row_)
        cnt = index+1
    out["user_list_size"] = cnt
    with open(input_.replace(".csv", "_pandas.json"), "w") as f:
        json.dump(out, f)
