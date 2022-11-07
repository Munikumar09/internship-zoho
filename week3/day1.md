## week 3: day 1  
#### 7 november 2022 
<h1 align="center"> JSON FILES IN PYTHON</h1>

**json**  
json is a javascript object notation. It stores the data in the form of key value pairs. Data stored inside the json file can be easily readable.  
**Read json file using python (niave way):**  
To read json file we have to open the file using open function. The `with` statement can be used  to group file operation statements within a block. The advantage of with statement is it will take care closing of file,after completing all operations automatically even in the case of exceptions also, and we are not required to close explicitly.`load` function is used to read the json file in the form of string and convert it into python dictionary or list of dictionaries.
```  
def load_data_file(file_name):
    with open(file_name,'r') as json_file:
        data=json.load(json_file)
        for items in data:
            for key,value in items.items():
                print("{0} : {1}".format(key,value))
```

**Writing data to json file**  
To write data to json file first we need to convert json string type to python object.
after that we can pass to the function `dump_data_file` as `data parameter` along with the file_name or path.
```
def dump_data_file(file_name,data):
    with open(file, 'w') as json_file:
        json.dump(data,json_file)
``` 
**append data to json file**  
To append or update the data to json file first we need to read the json file into a python object after that we can update the python object with the required data and re-write the json file with the updated data.
```
def update_json_data(data,file_name):
    with open(file_name,'r+') as json_file:
        new_data=json.load(json_file)
        new_data.append(data)
    with open(file_name,'w') as update_file:
        json.dump(new_data,update_file)
```

## JSON FILES WITH PANDAS  
we can read and write the json files using pandas.  
**Read the json files into pandas dataframe**  
reading json files into pandas dataframe is very easy and it can be done with few lines of code.
`read_json` method is used to read json files into a pandas dataframe.
```
def read_json_file(file_name):
    data=pd.read_json(file_name)
    return data
```
**Write the json files into a pandas dataframe**  
we convert JSON to dataframe by using json_normalize() method. After that we can write that datafram to file using to_json() method.  
```
def write_json_file(file_name,data,orient_type=None):
    df=pd.json_normalize(loaded_data)
    df.to_json(file_name,orient=orient_type)
```
## jsonl files in python  
jsonl format is also known as jsonlines. In jsonl each line is json object.jsonl is a convenient format for storing structured data that may be processed one record at a time. It follows `utf-8` encoding. Each line should be valid json value. we can use a newline character `\n` to separate records  
**To read the jsonl file in python**  
reading jsonl files is almost same as reading json files but we have to remove the newline character from each record.
```
def load_jsonl_data(file_name):
    container=[]
    with open(file_name,'r',encoding='utf-8') as reader:
        for line in reader.readlines():
            container.append(line.rstrip('\n|\r'))
        return container
```
**To write the jsonl files in python**  
To write the data to the jsonl file is similar to json but we have to ensure the encoding format as `utf-8` and also append a newline character at the end of each record to separate them.  
```
def dump_jsonl_data(file_name,data,append):
    mode='a+' if append else 'w'
    with open(file_name,mode,encoding='utf-8') as writer:
        for line in data:
            json_record=json.dumps(line)
            writer.write(json_record+"\n")
    print("{0} records written to the fiel".format(len(data)))
```
## jsonl files in pandas  
To read the jsonl files in pandas we have to pass the extra argument `lines` to the `read_json` function.  
**To read jsonl files in pandas**  
```
def read_json_file(file_name):
    data=pd.read_json(file_name,lines=True)
    return data
```

**To write the jsonl files in pandas**  
To write the jsonl files in pandas we have to pass the extra arguments `lines` as True and `orient` as records.
```
def write_json_file(file_name,data,is_lines):
    df=pd.json_normalize(loaded_data)
    df.to_json(file_name,lines=is_lines,orient="records")
```
<h1 align="center"> Streamlit</h1>

**columns**  
Insert containers laid out as side-by-side columns.  
```
col1,col2=st.columns(2)
with col1:
    #we can display what ever we want
with col2:
    #we can displat what ever we wan
```
**File uploader**  
To upload file we can use file uploder widget.  
```
uploaded_file=st.file_uploader
```
uploaded file will be stored inside the `uploaded_file` variable.  
**Success message**  
We need to show that a action or task has been successfully completed eg: uploading an image is successful then we have to display that the image was successfully uploaded. To do that we have to use `success` function  
```
st.success('Image was successfully uploaded!', icon="✅")
```
