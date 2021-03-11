import sys
import csv
import json

def csv_generator(path):
    with open(path, "r") as csv_:
        cnt = 0
        for row in csv.reader(csv_):
            if cnt > 0:
                split = row[0].split(" ")
                row_ = {
                    "list_id": cnt,
                    "first name": split[0],
                    "last name": split[1],
                    "email": row[1]
                }
                yield row_, cnt
            cnt = cnt + 1
            
if __name__ == "__main__":
    input_ = sys.argv[1]
    out = {
            "user_list":[]
        }
    for row, cnt in csv_generator(input_):
        out["user_list"].append(row)
        out["user_list_size"] = cnt
    with open(input_.replace(".csv", "_generator.json"), "w") as f:
        json.dump(out, f)
