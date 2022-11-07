import pandas as pd
import json

json_string = """
    [
        {
            "employee_id":"1234",
            "employee_name": "prabakar",
            "employee_age": "23",
            "employee_email": "prabakar@gmail.com"
        },
        {
            "employee_id":"3245",
            "employee_name": "ramraj",
            "employee_age": "25",
            "employee_email": "ramraj@gmail.com"
        },
        {
            "employee_id":"4332",
            "employee_name": "krishna",
            "employee_age": "22",
            "employee_email": "krishna@gmail.com"
        },
        {   "employee_id":"4234",
            "employee_name": "raveena",
            "employee_age": "24",
            "employee_email": "raveena@gmail.com"
        }
    
]
"""


def read_json_file(filename):
    data = pd.read_json(filename)
    print(data)


def write_json_file(file_name, data):
    loaded_data = json.loads(data)
    df = pd.json_normalize(loaded_data)
    df.to_json(file_name, orient="records")


def read_jsonl_file(file_name, is_jsonl=False):
    data = pd.read_json(file_name, lines=is_jsonl)
    return data


def write_jsonl_file(file_name, data, is_lines):
    loaded_data = json.loads(data)
    df = pd.json_normalize(loaded_data)
    df.to_json(file_name, lines=is_lines, orient="records")
