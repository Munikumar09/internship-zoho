## week 4: day 2  
#### 15 november 2022  

<h1 align="center"> Libraries </h1>  

Generally, libraries are lines of code written by you or others can you can use in your program.  
Python allows you to share functions or features with others as “modules”.  
### Random  
random is a library that comes with Python used to generate random things from a sequence or range.  
**choice**  
Inside the random module, there is a built-in function called `random.choice(seq)`.  
That function takes into it a sequence that is a list and outputs any one the value from the sequence.  
```
from random import choice

language = choice(["java","python","c++","kotlin","javascript"])
print(language)
```
**randint**  
This function will generate a random number between a and b.  

```
import Random

number = random.randint(1, 10)
print(number)
```

To suffle the items in a list we can use `shuffle` function from random  
### Statistics  
This module provides functions for calculating mathematical statistics of numeric data.  
This module contain the following functions:  
1. mean()  
2. mode()  
3. median()  
4. stdev(): simple standard deviation  

```
import statistics

print(statistics.mean([100, 90]))
```

### APIs  
requests is a package that allows your program to behave as a web browser would.  
In your terminal, type pip install requests.  

```
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())

```  

<h1 align="center"> File I/O</h1>  

As the part of programming requirement, we have to store our data permanently for
future purpose.  
File I/O is the ability of a program to take a file as input or create a file as output.  

Types of Files:  
There are 2 types of files  
1) Text Files:  
Usually we can use text files to store character data  
`Eg: abc.txt`  
2) Binary Files:  
Usually we can use binary files to store binary data like images,video files, audio files
etc...  

**Opening a File:**  
Before performing any operation (like read or write) on the file,first we have to open
that file.  
`f = open(filename, mode)`  
file opening modes for:  
<u>Text files:</u>  
r: read  
w: write  
a: append  
r+: read + write  
w+: write+read  
a+: write + read  
for binary files suffix with `b`  
eg: `rb,wb,ab,r+b,w+b,a+b`  

**closing file**  
After completion of operations on files it is highly recommended to close the file.  
`file.close()`  

**Writing Data to Text Files:**  
We can write character data to the text files by using the following 2 methods.  
1) write(str)  
2) writelines(list of lines)  
eg:  

```
f=open("myfile.txt",'w')
f.write("Python ")
list=["is ","used ","in ","machine learning"]
f.writelines(list)
f.close()
```

**Reading Character Data from Text Files:**  
We can read character data from text file by using the following read methods.  
read(): To read total data from the file  
read(n): To read 'n' characters from the file  
readline(): To read only one line  
readlines(): To read all lines into a list  

```
f=open("myfile.txt",'r')
data=f.read()
f.close()
```

**The with Statement:**  
The with statement can be used while opening a file.We can use this to group file
operation statements within a block.  
The advantage of with statement is it will take care closing of file,after completing all
operations automatically even in the case of exceptions also, and we are not required
to close explicitly.  

```
with open("myfile.txt","w") as f:
    f.write("java\n")
    f.write("python\n")
    f.write("dart\n")
```

**tell():**  
We can use tell() method to return current position of the cursor from
beginning of the file.  

**seek():**  
We can use `seek()` method to move cursor to specified location.  
`syntax: f.seek(offset, fromwhere)`  

**Handling CSV Files:**  

CSV : Comma seperated values  
As the part of programming, it is very common requirement to write and read data wrt csv files. Python provides `csv module` to handle csv files.  

```
import csv
with open("emp.csv","w") as f:
    w=csv.writer(f)
    w.writerow(["ENO","ENAME","ESAL","EADDR"])
    n=int(input("Enter Number of Employees:"))
    for i in range(n):
        eno=input("Enter Employee No:")
        ename=input("Enter Employee Name:")
        esal=input("Enter Employee Salary:")
        eaddr=input("Enter Employee Address:")
        w.writerow([eno,ename,esal,eaddr])
    print("Total Employees data written to csv file successfully")
```

**Reading Data from CSV File:**  

```
import csv
f=open("emp.csv",'r')
r=csv.reader(f)
data=list(r)
f.close()
```

<h1 align="center"> Exceptions</h1>  

Runtime errors also known as exceptions.  
While executing the program if something goes wrong because of end user input or
programming logic or memory problems etc then we will get Runtime Errors.  
Simply, an exception is an unwanted and unexpected event that disturbs normal flow of program is called exception.  
Exception handling means we have to define alternative way to continue rest of the program normally when exception occured.  

**Exception Handling by using try-except:**  

The code which may raise exception is called risky code and we have to take risky code
inside try block. The corresponding handling code we have to take inside except block.  

```
try:
    Risky Code
except exception_type:
    Handling code/Alternative Code
```
eg:  

```
try:
    print(10/0)
except ZeroDivisionError as msg:
    print("exception raised and its description is:",msg)
```

**try with Multiple except Blocks:**  

The way of handling exception is varied from exception to exception.Hence for every exception type a seperate except block we have to provide.  

Eg:  
```
try:
    risky code
except ZeroDivisionError:
    perform alternative arithmetic operations
except FileNotFoundError:
    use alternative file
```  

**Default except Block:**  

We can use default except block to handle any type of exceptions.  
In default except block generally we can print normal error messages.  

```except :
    print("general error message")
```

It should be placed at the end of try-except statements.  

**finally Block:**  
It is not recommended to maintain clean up code inside try or catch blocks because there is no guarentee for the execution of every statement inside try or catch blocks always.  
The speciality of finally block is it will be executed always whether exception raised or not
raised and whether exception handled or not handled.  
Hence the main purpose of finally block is to maintain clean up code.  

```
try:
    Risky Code
except:
    Handling Code
finally:
    Cleanup code
```

**else Block with try-except-finally:**  
We can use else block with try-except-finally blocks.  
else block will be executed if and only if there are no exceptions inside try block.  

**User Defined Exceptions**  
Some time we have to define and raise exceptions explicitly to indicate that something
goes wrong, such type of exceptions are called User Defined Exceptions or Customized
Exceptions  
To raise an exception we have to use `raise` keyword.  
Every exception in Python is a class that extends Exception class either directly or
indirectly.  

```
Syntax:
class classname(predefined exception class name):
    def __init__(self,arg):
    self.msg=arg
raise classname(message)
```
