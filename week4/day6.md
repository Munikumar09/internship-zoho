## week 4: day 6  
#### 19 november 2022  
<h1 align="center"> Comprehension </h1>  
In python, comprehensions provide us a short and concise way to construct new sequences (such as lists, set, dictionary etc.) using sequences which have been already defined.  

Python supports the following 3 types of comprehensions:  

1. List Comprehensions  
2. Dictionary Comprehensions  
3. Set Comprehensions  

**List Comprehensions:**  
It is very easy and compact way of creating list objects from any iterable objects (Like List, Tuple, Dictionary, Range etc) based on some condition.  
`syntax : output_list = [output_exp for var in input_list if (var satisfies this condition)]`  
```
def is_prime(num):
    count=0
    for i in range(1,num//2+1):
        if num%i == 0:
            count+=1
        if count>1:
            return False
    return True
    
odd_nums=[x for x in range(1,30) if x%2==1]
prime_nums=[num for num in odd_nums if is_prime(num) ]
```
**Dictionary Comprehensions:**  
Extending the idea of list comprehensions, we can also create a dictionary using dictionary comprehensions. The basic structure of a dictionary comprehension looks like below.  

`output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}`  
```
states = [
    "Andhra Pradesh",
    "Assam",
    "Bihar ",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
]
capitals = [
    "Amaravati",
    "Itanagar",
    "Dispur",
    "Patna",
    "Naya Raipur",
    "Panaji",
    "Gandhinagar",
    "Chandigarh",
    "Shimla ",
    "Dharamsala",
]
states_capital_dict={f"{state} : {capital}" for state , capital in zip(states,capitals)}
print(states_capital_dict)
```
**Set Comprehensions:**  
Set comprehensions are pretty similar to list comprehensions. The only difference between them is that set comprehensions use curly brackets { }.  
```
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
  
set_using_comp = {var for var in input_list if var % 2 == 0}
  
print("Output Set using set comprehensions:" set_using_comp)
```
### Enumerate  
Often, when dealing with iterators, we also get need to keep a count of iterations. Python eases the programmers’ task by providing a built-in function enumerate() for this task. Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object. This enumerated object can then be used directly for loops or converted into a list of tuples using the list() method.  
`Syntax: enumerate(iterable, start=0)`  
```
states = [
    "Andhra Pradesh",
    "Assam",
    "Bihar ",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
]
for index,state in enumerate(states,start=1):
    print(f"{index} : {state}")
```
### Iteration  
A process that is repeated more than one time by applying the same logic is called an Iteration.  
**Iterator**  
An iterator is an object which contains a countable number of values and it is used to iterate over iterable objects like list, tuples, sets, etc.  

Using an iterator-  
iter() keyword is used to create an iterator containing an iterable object.  
next() keyword is used to call the next element in the iterable object.  
We can create our own iterator classes by implementing the `__iter__` and `__next__` methods as follows:  
```
class NumGenerator:
    def __init__(self, num_limit):
        self.num_limit = num_limit

    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):
        x = self.x
        if x > self.num_limit:
            raise StopIteration
        self.x = x + 1
        return x
num_generator = NumGenerator(20)
itr=num_generator.__iter__()
for it in itr:
    print(it)
```
we can create iterators for the iterable objects such as lists, tuples, dictionaries etc.  
```
states = [
    "Andhra Pradesh",
    "Assam",
    "Bihar ",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
]
itr=iter(states)
try:
    while True:
        print(next(itr))
except StopIteration:
    ...
```
### Generators  
Generator is a function which is responsible to generate a sequence of values.  
We can write generator functions just like ordinary functions, but it uses yield keyword to
return values.  
**Advantages of Generator Functions:**  
1) When compared with Class Level Iterators, Generators are very easy to use.  
2) Improves Memory Utilization and Performance.  
3) Generators are best suitable for reading Data from Large Number of Large Files.  

To countdown the number from max to min:  
```   
def countdown(num):
    print("Start Countdown")
    while(num>0):
        yield num
        num=num-1
values=countdown(5)
for x in values:
print(x)
```
To print the Fibonacci series using generators:  

```
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for f in fib():
    if f>100:
        break
    print(f)
```