## week 2: day 6  
#### 5 november 2022 
<h1 align="center"> Numpy</h1>
NumPy is a Python library used for working with arrays. numpy array operations are very fast as compared to list in python.  
To create a numpy array:  
```
a=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
])
```
To create a numpy array from python list:  
```
l=[1,2,3,4]
a=np.array(l)
```
To get dimension of an array:  
```
a.shape()
```
To get total number of elements in an array:  
```
a.size()
```
To access the elements of an array:  
for 1-d array:  
```
a[index]
```
for 2-d array:  
```
a[row][col]
    or
a[row,col]
```
To transport a matrix:  
```
a.T
```
Slicing in matrix:  
syntax for slicing in matrix is `a[start_row:end_row,start_col,end_col]`
```
a=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
])
print(a[1:5,3:5])
```
To get all the diagonal elements in an matrix:  
```
np.diagonal(a)
```
Boolean indexing:  
To filter all the elements based on a condition we use boolean indexing.  
Eg: To filter all the even numbers in the matrix:  
```
import numpy as np
a=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
])
b=np.where(a%2,a,0)
print(b)
```
Reshape:  
to rearange the elements in rows and columns of diffrent size:  
```
aa=np.array([[1,2,3,4,5,6],
            [7,8,9,10,11,12],
            [13,14,15,16,17,18]
            ])
aa=aa.reshape((2,9))
print(aa)
```
<h1 align="center">pandas</h1>  
Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.  
Series:  
A Pandas Series is like a column in a table.
Series are built on top of NumPy arrays.  

Create a series by first creating a list:  
``` 
list_1 = ['a', 'b', 'c', 'd']

labels = [1, 2, 3, 4]
ser_1 = pd.Series(data=list_1, index=labels)
```
Creating Series from NumPy array:  
```
arr_1 = np.array([1, 2, 3, 4])
ser_2 = pd.Series(arr_1)
```
Creating Series from dictionary:  
```
dict_1 = {"f_name": "Derek", 
              "l_name": "Banas", 
              "age": 44}
ser_3 = pd.Series(dict_1)
```
We can perform math operation in Series:  
```
ser_2 + ser_2
ser_2 - ser_2
ser_2 * ser_2
ser_2 / ser_2
```
**DataFrame**  
Dataframe is like a table with rows and columns.  
Create random matrix 4x4 with values between 10 and 50  
```
arr_2=np.random.randint(10,50,size=(4,4))
```
Create DF with data, row labels & column labels  
```
df_1=pd.DataFrame(arr_2,['A','B','C','D'],['W','X','Y','Z'])
```
Create a DF from multiple series in a dict If series are of different lengthes extra spaces are NaN  
```
dict_3={
    'one':pd.Series([1,2,3,4],index=['a','b','c','d']),
    'two':pd.Series([10,20,30],index=['a','b','c'])
}
```
You can assign the keys as row labels and column labels separate  
with orient='index'
```
pd.DataFrame.from_dict(dict([
    ('A',[1,2,3]),('B',[4,5,6])
]),orient='index',columns=['one','two','three'])
```
Get number of rows and columns as tuple  
```
print(df_1.shape)
```
<h1 align="center">Streamlit</h1>  
Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time.  
To display any sort of data we can use `write` function in streamlit. It displays the data based on it type.  
```
st.write(pd.dataframe(
    'one':pd.Series([1,2,3,4],index=['a','b','c','d']),
    'two':pd.Series([10,20,30],index=['a','b','c'])
))
```

**Text widgets**  
Text widgets are used to display the text data.  
st.markdown  is used to display text in markdown format.  
```
st.markdown("""
# markdown text of the web app
""")
```
st.title is used to set the tile of the web app  
```
st.title("Welcome to streamlit Tool")
```
similarly we can use `st.header`, `st.subheader`, `st.text`.  

**chart elements**  
chart elements are used to display the data in the form of a chart.  
st.line_chart  
```
st.line_chart(data_frame)
```
similarly we can use `st.area_chart`, `st.bar_chart`, etc.  

**Input widgets**
Input widgets are used to take input from the user (interactive).  
st.button  
```
st.button("submit")
```
st.button returns boolean value i.e if pressed true else false.  
**st.text_input**  
```
st.text_input("enter text")
```
Similarly there are various input widgets for different purposes.  

Based on the learnings I developed a small stock price history tracker. It takes the stock symbol as input from the user and retrives the data related to that stock from yahoo finance by using yfinance tool. Code related to the learning is placed inside the code folder.  