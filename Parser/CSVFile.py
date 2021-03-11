import sys
import csv
import json

if __name__ == "__main__":
    input_ = sys.argv[1]
    with open(input_) as f:
        data = csv.reader(f, delimiter=",")
        cnt = 0
        out = {
            "user_list":[]
        }
        for row in data:
            split = row[0].split(" ")
            if cnt > 0:
                row_ = {
                    "list_id": cnt,
                    "first name": split[0],
                    "last name": split[1],
                    "email": row[1]
                }
                out["user_list"].append(row_)
            cnt = cnt + 1
        out["user_list_size"] = cnt-1
    with open(input_.replace(".csv", "_file.json"), "w") as f:
        json.dump(out, f)
