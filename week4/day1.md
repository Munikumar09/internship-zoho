## week 4: day 1  
#### 14 november 2022 
<h1 align="center"> Python Functions</h1>  

If a group of statements is repeatedly required then We can to define these statements as a single unit and we can call that unit any number of times based on our requirement without
rewriting. This unit is known as function.  
The main advantage of functions is code Reusability.  
Python supports 2 types of functions  
1) Built in Functions  
2) User Defined Functions  
### Built in Functions:  
The functions which are coming along with Python software automatically, are called
built in functions or pre defined functions.  
Eg:  
>type()
>input()
>print()

### User Defined Functions:  
The functions which are developed by programmer explicitly according to business
requirements, are called user defined functions.  
Syntax to Create User defined Functions:  
```
def function_name(parameters) :
""" doc string"""
----
-----
return value
```
In Python, a function can return any number of values.  
### Types of Arguments  
There are 4 types are actual arguments are allowed in Python.  
1) Positional Arguments  
2) Keyword Arguments  
3) Default Arguments  
4) Variable Length Arguments  

**1.Positional Arguments:**  
These are the arguments passed to function in correct positional order.  
```
def sub(a, b):
    print(a-b)
sub(100, 200) # -100
sub(200, 100) # 100
```
**2.Keyword Arguments:**  
We can pass argument values by keyword i.e by parameter name.  
```
def wish(name,msg):
    print("Hello",name,msg)
wish(name="Muni",msg="Good Morning")
```
Here the order of arguments is not important but number of arguments must be matched.  
**3.Default Arguments:**  
Sometimes we can provide default values for our positional arguments.  
```
def wish(name="Guest"):
    print("Hello",name,"Good Morning")
wish("Muni") # Hello Muni Good Morning
wish() # Hello Guest Good Morning
```
If we are not passing any name then only default value will be considered.  
**4.Variable Length Arguments:**  
Sometimes we can pass variable number of arguments to our function, such type of
arguments are called variable length arguments.  
We can declare a variable length argument with * symbol as follows:  
`def f1(*n):`  
eg:  

```
def sum(*n):
    total=0
    for n1 in n:
        total=total+n1
    print("The Sum=",total)
sum(10,20,30,40) #The Sum= 100
```
**Anonymous Functions:**  
Sometimes we can declare a function without any name,such type of nameless
functions are called anonymous functions or lambda functions.  
The main purpose of anonymous function is just for instant use(i.e for one time usage)  
Syntax of lambda Function: `lambda argument_list : expression`  
eg: 
```
s=lambda n:n*n
print("The Square of 4 is :",s(4)) # 16
```
**filter() Function:**  
We can use filter() function to filter values from the given sequence based on some
condition.  
`Syntax: filter(function,sequence)`
eg:  
```
# filtering even numbers
l=[0,5,10,15,20,25,30]
l1=list(filter(lambda x:x%2==0,l))
print(l1) #[0,10,20,30]
```
**map() Function:**  
For every element present in the given sequence,apply some functionality and
generate new element with the required modification. For this requirement we
should go for map() function.  
`Syntax: map(function, sequence)`  
eg:  
```
# To find square of given numbers
l=[1,2,3,4,5]
l1=list(map(lambda x:x*x,l))
print(l1) #[1, 4, 9, 16, 25]
```
**reduce() Function:**  
reduce() function reduces sequence of elements into a single element by applying the
specified function.  
`Syntax: reduce(function,sequence)`  
eg:  
```
# To find sum of given numbers
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result) # 150
```
*Problem set solution are placed inside code folder.*  
<h1 align="center">Conditionals</h1>  

Conditionals allow the programmer, to allow the program to make decisions: As if the program has the choice between two options based upon certain conditions.  
conditional statements are:  

**if statement**  
If condition is true then statements will be executed.  
```
if condition :
statement-1
statement-2
statement-3
```
**if-else:**  
```
if condition:
Action-1
else:
Action-2
```
if condition is true then Action-1 will be executed otherwise Action-2 will be executed.  
**if-elif-else:**  
```
if condition1:
Action-1
elif condition2:
Action-2
...
else:
Default Action
```
Based on the condition the corresponding action will be executed.  
**match**  
A match statement compares the value following the `match` keyword with each of the values following the `case` keywords. In the event a match is found, the respective indented code section is executed and the program stops the matching.  
```
syntax:
match term:
    case pattern-1:
         action-1
    case pattern-2:
         action-2
    case pattern-3:
         action-3
    case _:
        action-default
```
*Problem set solution are placed inside code folder.*  
<h1 align="center"> Iterative Statements or Loops </h1>  

If we want to execute a group of statements multiple times then we should have to use
Iterative statements.  
Python supports 2 types of iterative statements.  
1) for loop  
2) while loop  

**pass statement:**  
pass is a keyword in Python.  
In our programming syntactically if block is required which won't do anything then we
can define that empty block with pass keyword.  

*Problem set solution are placed inside code folder.*