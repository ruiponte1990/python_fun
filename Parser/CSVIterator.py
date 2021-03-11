import sys
import csv
import json

class CSVIterator():
    """
    Implementation of an iterator that can parse CSV files.
    """
    def __init__(self, path):
        self.path = path
        self.value = 0
        self.file  = open(self.path, "r")

    def __iter__(self):
        return self

    def __next__(self):
        line = next(self.file)
        if line:
            next_val = self.value
            self.value =  self.value + 1
            if next_val > 0:
                row = line.split(",")
                name = row[0]
                split = name.split(" ")
                row_ = {
                    "list_id": next_val,
                    "first name": split[0],
                    "last name": split[1],
                    "email": row[1]
                }
                return row_, next_val
            else:
                return line, 0
        else:
            self.file.close()
            raise StopIteration()

if __name__ == "__main__":
    input_ = sys.argv[1]
    out = {
        "user_list" : []
    }
    for row, cnt in CSVIterator(input_):
        if cnt > 0:
            out["user_list"].append(row)
            out["user_list_size"] = cnt
    with open(input_.replace(".csv", "_iterator.json"), "w") as f:
        json.dump(out, f)

