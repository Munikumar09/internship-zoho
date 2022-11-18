## week 4: day 5  
#### 18 november 2022  
<h1 align="center"> Polymorphism </h1>  

### Duck Typing Philosophy of Python:  
In Python we cannot specify the type explicitly. Based on provided value at runtime the type will be considered automatically. Hence Python is considered as Dynamically Typed Programming Language.  
We cannot decide type of object at the Beginning. At Runtime we can Pass any Type.
At runtime if 'it walks like a duck and talks like a duck,it must be duck'. Python follows this principle. This is called Duck Typing Philosophy of Python.  
EG:  
```
class Duck:
    def talk(self):
        print('Quack.. Quack..'
class Dog
    def talk(self)
        print('Bow Bow..')
class Cat:
    def talk(self):
        print('Moew Moew ..')
class Goat:
    def talk(self):
        print('Myaah Myaah ..')
def call_talk(obj):
    obj.talk()
l=[Duck(),Cat(),Dog(),Goat()]
for obj in l:
    call_takl(obj)
```

The problem in this approach is if obj does not contain talk() method then we will get AttributeError.  
But we can solve this problem by using hasattr() function.  
`hasattr(obj,'attributename')` : attributename can be Method Name OR Variable Name  

```
def call_takl(obj):
    if hasattr(obj, "talk"):
        obj.talk()
    else:
        print(f"{type(obj)} do not have 'talk' method)
```

## 2) Overloading  
We can use same operator or methods for different purposes.  
There are 3 types of Overloading  
1) Operator Overloading  
2) Method Overloading  
3) Constructor Overloading  

**1)  Operator Overloading:**  
We can use the same operator for multiple purposes, which is nothing but operator
overloading.  
Python supports operator overloading.  
Eg 1: + operator can be used for Arithmetic addition and String concatenation  
```
print(10+20)#30
print('muni '+'kumar')#muni kumar
```

Eg 2: * operator can be used for multiplication and string repetition purposes.  
```
print(10*20)#200
print('muni '*3)#muni muni muni 
```

For every operator Magic Methods are available. To overload any operator we have to override that Method in our class.  
Internally + operator is implemented by using `__add__()` method.This method is called magic method for + operator. We have to override this method in our class.  

```
class Book:
    def __init__(self,pages,title):
        self.pages=pages
        self.title=title
    def __add__(self,other_book):
        return self.pages+other_book.pages
    def __eq__(self, other_book):
        return self.title==other_book.title and self.pages==other_book.pages
    def __gt__(self,other_book):
        return self.pages>other_book.pages
book1=Book(178,"Atomic habits")
book2=Book(345,"intelligent investor")
book3=Book(178,"Atomic habits")
print(f"Total pages:{book1+book2}")
print(book1==book3)
print(book2>book1)
```

similarly there are magic methods available for most of the other operators.  

```
+ :object.__add__(self,other)
- :object.__sub__(self,other)
* :object.__mul__(self,other)
/ :object.__div__(self,other)
// :object.__floordiv__(self,other)
% :object.__mod__(self,other)
** :object.__pow__(self,other)
...
```

**2) Method Overloading:**  
If 2 methods having same name but different type of arguments then those methods are said to be overloaded methods.  
```
Eg: 
m1(int a)
m1(double d)
```
But in Python Method overloading is not possible.  
If we are trying to declare multiple methods with same name and different number of arguments then Python will always consider only last method.  

We can handle Overloaded Method Requirements in Python:  

Most of the times, if method with variable number of arguments required then we can handle with default arguments or with variable number of argument methods.  

```
class Calculator:
    def add(self,*n:tuple):
        ans=0
        for element in n:
            ans+=element
        return ans
    def mul(slef,*n):
        ans=1
        for element in n:
            ans*=element
        return ans
    
calculator=Calculator()
print(calculator.add())
print(calculator.add(10,20))
print(calculator.add(30,20,40))
print(calculator.mul(19,39))
print(calculator.mul(23,32,23))
```

**3) Constructor Overloading:**  
Constructor overloading is not possible in Python.  
If we define multiple constructors then the last constructor will be considered.  
But based on our requirement we can declare constructor with default arguments and variable number of arguments.  
### 3) Overriding  
**Method Overriding**  
What ever members available in the parent class are bydefault available to the child class through inheritance. If the child class not satisfied with parent class implementation then child class is allowed to redefine that method in the child class based on its requirement. This concept is called overriding.  
Overriding concept applicable for both methods and constructors.  
**Constructor Overriding**  
if child class does not contain constructor then parent class constructor will be executed
From child class constuctor we can call parent class constructor by using super() method.  
eg: 
```
class Person:
    def __init__(self,name:str,age:int) -> None:
        self.name=name
        self.age=age
    def work(self):
        print("Working in industry")
    def display(self):
        print(f"name: {self.name}\nage: {self.age}")
class Employee(Person):
    def __init__(self,name:str,age:int,emp_id:int,emp_email:str) -> None:
        super().__init__(name,age)
        self.emp_id=emp_id
        self.emp_email=emp_email
    def work(self):
        print("Working in Software industry")
    def display(self):
        super().display()
        print(f"employee id: {self.emp_id}\nemployee email: {self.emp_email}")
employee=Employee("rajesh",23,3244,"rajesh.rj@example.com")
employee.display()
employee.work()
```
## Abstraction  
**Abstract Method:**  

Sometimes we don't know about implementation, still we can declare a method. Such types of methods are called abstract methods.i.e abstract method has only declaration but not implementation.  
In python we can declare abstract method by using `@abstractmethod` decorator as
follows.  

```
@abstractmethod
def m1(self): pass
```
Child classes are responsible to provide implemention for parent class abstract methods.  

**Abstract class:**  
Some times implementation of a class is not complete,such type of partially
implementation classes are called abstract classes.  
Every abstract class in Python shouldbe derived from `ABC` class which is present in abc module.  
If a class contains atleast one abstract method and if we are extending ABC class then instantiation is not possible.  

simply, "abstract class with abstract method instantiation is not possible".  

Parent class abstract methods should be implemented in the child classes. Otherwise we cannot instantiate child class.If we are not creating child class object then we won't get
any error.  

Abstract class can contain both abstract and non-abstract methods also.  
```
class Shape(ABC):
    @abstractmethod
    def no_of_sides(self)-> None:
        pass
    def type_of_shape(self)-> None:
        print("Two-dimensional shape")
class Square(Shape):
    def no_of_sides(self)-> None:
        return 4
    
square=Square()
print(square.no_of_sides())
```
**Interface:**  
In general if an abstract class contains only abstract methods such type of abstract class is considered as interface.  
```
from abc import ABC, abstractmethod
import sys


class DBInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class IBMDatabase(DBInterface):
    def connect(self):
        print("connecting to IBM database...")

    def disconnect(self):
        print("Disconnecting from IBM database...")


class OracleDatabase(DBInterface):
    def connect(self):
        print("connecting to Oracle database...")

    def disconnect(self):
        print("Disconnecting from Oracle database...")


database_name = input("Enter database name to connect: ")
try:
    database = globals()[database_name]
except KeyError:
    sys.exit("Database Not Found: " + database_name)
database_obj = database()
database_obj.connect()
database_obj.disconnect()
```
he inbuilt function `globals()[str]` converts the string 'str' into a class name andreturns the classname and if class not found it raises `KeyError`.  

**Public, Protected and Private Attributes:**  
**Public**  
By default every attribute is public. We can access from anywhere either within the class or from outside of the class.  
`Eg: name = 'durga'`  
**Protected**  
Protected attributes can be accessed within the class anywhere but from outside of the class only in child classes. We can specify an attribute as protected by prefexing with `_` symbol.  
```
Syntax: _variablename = value
Eg: _name='muni'
```
But is is just convention and in reality does not exists protected attributes.  
**Private**  
private attributes can be accessed only within the class.i.e from outside of the class we cannot access. We can declare a variable as private explicitly by prefexing with 2 underscore symbols.  
```
syntax: __variablename=value
Eg: __name='muni'
```
But in python, we can access the private attributes of the class indirectly by following line of code:  
`objectreference._classname__variablename`  

```
class Profile:
    def __init__(self, name: str, email: str, password: str) -> None:
        self.name = name
        self._email = email
        self.__password = password


profile = Profile("Test", "test@example.com", "Test123")
print(profile.name)
print(profile._email)
print(profile._Profile__password)
```
**Encapsulation:**  
Encapsulation is the process of binding the data (variables) and code acting on the data (methods) together as a single unit(like class).  
In encapsulation, the variables of a class will be hidden from other classes, and can be accessed only through the methods of their current class.  
```
import sys


class Profile:
    existing_users: list[
        str,
    ] = ["muni09", "muni08", "muni11"]

    def __init__(self, name: str, username: str, email: str) -> None:
        try:
            self.name = name
            self.email = email
            self.username = username
        except ValueError as e:
            sys.exit(f"cannot create account because: {e}")
        else:
            print("Account created successfully")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        if username not in self.existing_users:
            self.__username = username
        else:
            raise ValueError(f"{username} Username already exists")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def __str__(self):
        return f"name: {self.name}\nusername: {self.username}\nemail: {self.email}"


profile = Profile("Munikumar", "muni09", "muni@gmail.com")
print(profile)
profile.username = "muni"
```
