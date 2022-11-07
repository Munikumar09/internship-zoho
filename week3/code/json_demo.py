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
dict_python = json.loads(json_string)


def dump_jsonl_data(
    file_name,
    data,
    append,
):
    mode = "a+" if append else "w"
    with open(file_name, mode, encoding="utf-8") as writer:
        for line in data:
            json_record = json.dumps(line)
            writer.write(json_record + "\n")
    print("{0} records written to the fiel".format(len(data)))


def load_jsonl_data(file_name):
    container = []
    with open(file_name, "r", encoding="utf-8") as reader:
        for line in reader.readlines():
            container.append(line.rstrip("\n|\r"))
        return container


def dump_data_file():
    with open("sample.json", "w") as json_file:
        json.dump(dict_python, json_file)


def load_data_file():
    with open("sample.json", "r") as json_file:
        data = json.load(json_file)
        print(type(data))
        i = 0
        for items in data:
            for key, value in items.items():
                print("{0} : {1}".format(key, value))
            print("__________________________________________________")
            i += 1


def update_json_data(data, file_name="sample.json"):
    with open(file_name, "r+") as json_file:
        new_data = json.load(json_file)
        new_data.append(data)
    with open(file_name, "w") as update_file:
        json.dump(new_data, update_file)
