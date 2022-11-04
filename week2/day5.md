## week 2: day 5  
#### 4 november 2022 
<h1 align="center"> Pandas </h1>  
pandas is a python library used for working with data sets. Pandas allow us to analyze big data and make conclusions based on statistical theories. Pandas can clean messy data sets and make them readable and relavant.  

### Series:  
A panda series is like a column in a table. Pandas Series will be created by loading the datasets from existing storage, storage can be SQL Database, CSV file, and Excel file.
To create panda series from list:  
```
import pandas as pd
cars=["volvo","BMW","Audi","Honda","Hyndai","Tata","jaguar"]
my_car_series=pd.Series(cars)
```
__Accessing Element from Series with Position__ :  
Use the index operator [ ] to access an element in a series. The index must be an integer. In order to access multiple elements from a series, we use Slice operation.  
```
my_car_series[0]
my_car_series[0:3]
```
__Accessing Element Using Label (index)__ :  
In order to access an element from series, we have to set values by index label. A Series is like a fixed-size dictionary in that you can get and set values by index label.  
```
my_car_series_custome_lable=pd.Series(cars,index=["sweden","Germany","Germany","Japan","south Korea","India","UK"])
print(my_car_series_custome_lable['Japan'])
```
we can also use loc[] and iloc functions to access the data inside the series.  
__Binary Operations on series__  
We can perform binary operation on series like addition, subtraction etc. In order to perform binary operation on series we have to use some function like .add(),.sub() etc..  
```
import pandas as pd
first=pd.Series([1,2,3,4,5,6,7,8,9,10,11])
second=pd.Series([10,20,30,40,50,60,70,80,90,100,110])
output=first.add(second,fill_value=0)
print(output)
```
__conversion operation__  
In conversion operation we perform various operation like changing datatype of series, changing a series to list etc. In order to perform conversion operation we have various function which help in conversion like .astype(), .tolist() etc.  
```
import pandas as pd
nifty=pd.read_csv("data/nifty_data.csv")

dtype_before=nifty.dtypes
nifty["Open"]=nifty["Open"].astype(int)
dtype_after=nifty.dtypes
print(dtype_before)
print("_____________________")
print(dtype_after)
```
### Dataframes:  
DataFrame: A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.  
we can create dataframes by loading the datasets from existing storage, storage can be CSV file, and Excel file. Pandas DataFrame can be created from the lists, dictionary, and from a list of dictionary etc.  
Creating dataframe from dictionary:  
``` 
import pandas as pd
import numpy as np
student_marks={
    "name":["muni","phani","lokesh","raj","mohan"],
    "operating system":[88,78,83,55,77],
    "computer network":[77,86,66,54,np.nan],
    "DBMS":[75,56,55,63,76]
}
marks_dataframe=pd.DataFrame(student_marks)
```
To create dataframe from csv file:  
```
nifty_dataframe=pd.read_csv("data/nifty_data.csv")
print(type(nifty_dataframe))
```
__Indexing a Dataframe using indexing operator [ ] :__  
Indexing operator is used to refer to the square brackets following an object. The .loc and .iloc indexers also use the indexing operator to make selections.  
```
nifty_dataframe=pd.read_csv("data/nifty_data.csv",index_col="Date")
print(nifty_dataframe.loc["25-Oct-2022"])
```
__Column Selection:__   
In Order to select a column in Pandas DataFrame, we can either access the columns by calling them by their columns name.  
```
import pandas as pd
student_marks={
    "name":["muni","phani","lokesh","raj","mohan"],
    "operating system":[88,78,83,55,77],
    "computer network":[77,86,66,54,45],
    "DBMS":[75,56,55,63,76]
}

# creating student_marks dataframe
marks_dataframe=pd.DataFrame(student_marks)
#accessing columns of dataframe
print(marks_dataframe[["name","operating system","DBMS"]])
```
__missing values__  
To show missing values we can use .isnull() function, it prints True if value is missing else prints False.  
```
print(marks_dataframe.isnull())
```
__Filling missing values:__  
we can fill the missing values by using fillna(),replace() and interpolate() functions ans these functions replaces the missing values with their own values.  
```
import pandas as pd
import numpy as np
marks= {'DBMS':[100, 90, np.nan, 95],
        'OS': [30, 45, 56, np.nan],
        'CN':[np.nan, 40, 80, 98]}
marks_df = pd.DataFrame(dict)
df.fillna(0)
```
Here we are filling the missing values with value 0.  
__Dropping missing values__:  
If a record contain missing values, we may not need that record for analysis at that time we can remove or drop that record.  
In order to drop a null values from a dataframe, we used dropna() function this fuction drop Rows/Columns of datasets with Null values.  
```
import pandas as pd
import numpy as np
marks= {'DBMS':[100, 90, np.nan, 95],
        'OS': [30, 45, 56, np.nan],
        'CN':[np.nan, 40, 80, 98]}
marks_df = pd.DataFrame(dict)
df.dropna()
```
__Iterating over rows :__  
In order to iterate over rows, we can use three function iteritems(), iterrows(), itertuples().   
```
import pandas as pd
student_marks={
    "name":["muni","phani","lokesh","raj","mohan"],
    "operating system":[88,78,83,55,77],
    "computer network":[77,56,66,54,65],
    "DBMS":[75,56,55,63,76]
}
marks_df=pd.DataFrame(student_marks)
for row, val in marks_df.iterrows():
    print(row, val)
    print()
```
__Iterating over columns :__

```
import pandas as pd
student_marks={
    "name":["muni","phani","lokesh","raj","mohan"],
    "operating system":[88,78,83,55,77],
    "computer network":[77,56,66,54,65],
    "DBMS":[75,56,55,63,76]
}
marks_df=pd.DataFrame(student_marks)
columns=list(marks_df)
for i in columns:
    print(marks_df[i][0])
```
Practice code placed in the code folder with name `pandas-practice`