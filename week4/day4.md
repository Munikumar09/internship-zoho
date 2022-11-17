## week 4: day 4  
#### 17 november 2022 
<h1 align="center"> Object Oriented Programming </h1>  

**What is Class:**  
In Python every thing is an object. To create objects we required some Model or Plan
or Blue print, which is nothing but class.  
We can write a class to represent properties (attributes) and actions (behaviour) of 
object.  
1. Properties can be represented by variables  
2. Actions can be represented by Methods.  

Hence class contains both variables and methods.  

```
Syntax:
class className:
''' documenttation string '''
    variables:instance variables,static and local variables
    methods: instance methods,static methods,class methods
```
Within the Python class we can represent data by using variables.  
that means There are 3 types of variables are allowed.  
1) Instance Variables (Object Level Variables)  
2) Static Variables (Class Level Variables)  
3) Local variables (Method Level Variables)  

Within the Python class, we can represent operations by using methods. The following are
various types of allowed methods  
1) Instance Methods  
2) Class Methods  
3) Static Methods  

```
class Student:
''''' This is student class with required data'''
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
    def display(self):
        print("Student Name:{}\nRollno:{} \nMarks:{}".format(self.name,self.rollno,self
        .marks))
student=Student("Munikumar",101,80)
student.display()

```
**Self Variable:**  
self is the default variable which is always pointing to current object (like this keyword
in Java)  
By using self we can access instance variables and instance methods of object.  
**constructor:**  
Constructor is a special method in python.  
The name of the constructor should be `__init__(self)`  
The main purpose of constructor is to declare and initialize instance variables.  
Constructor can take atleast one argument(atleast self)  
Constructor is optional and if we are not providing any constructor then python will
provide default constructor.  

**1) Instance Variables:**  
If the value of a variable is varied from object to object, then such type of variables are
called instance variables.  
For every object a separate copy of instance variables will be created.  
We can declare the instance variables in the following places:  
1) Inside Constructor by using self variable  
2) Inside Instance Method by using self variable  
3) Outside of the class by using object reference variable  

**2) Static Variables:**  
If the value of a variable is not varied from object to object, such type of variables we
have to declare with in the class directly but outside of methods. Such types of
variables are called Static variables.  
For total class only one copy of static variable will be created and shared by all objects
of that class.  
We can access static variables either by class name or by object reference. But most often we use class name.  
We can declare the static variables in the following places:  
1) In general we can declare within the class directly but from out side of any method  
2) Inside constructor by using class name  
3) Inside instance method by using class name  
4) Inside classmethod by using either class name or cls variable  
5) Inside static method by using class name  

```
class Test:
    a=10
    def __init__(self):
        Test.b=20
    def m1(self):
        Test.c=30
    @classmethod
    def m2(cls):
        cls.d1=40
        Test.d2=400
    @staticmethod
    def m3():
        Test.e=50
t=Test()
Test.f=60
print(Test.__dict__)
```

**3) Local Variables:**  
Sometimes to meet temporary requirements of programmer,we can declare variables inside a method directly,such type of variables are called local variable or temporary variables.  
Local variables will be created at the time of method execution and destroyed once method completes.  
Local variables of a method cannot be accessed from outside of method.  
**1) Instance Methods:**  
Inside method implementation if we are using instance variables then such type of
methods are called instance methods.  
Inside instance method declaration, we have to pass self variable. `def m1(self)`:  
By using self variable inside method we can able to access instance variables.  
Within the class we can call instance method by using self variable and from outside of
the class we can call by using object reference.  
**2) Class Methods:**  
Inside method implementation if we are using only class variables (static variables),
then such type of methods we should declare as class method.    
We can declare class method explicitly by using `@classmethod` decorator.  
For class method we should provide `cls` variable at the time of declaration  
We can call classmethod by using classname or object reference variable.  
**3) Static Methods:**  
In general these methods are general utility methods.  
Inside these methods we won't use any instance or class variables.  
Here we won't provide self or cls arguments at the time of declaration.  
We can declare static method explicitly by using `@staticmethod` decorator.  
We can access static methods by using classname or object reference.  
**inner class**  
Sometimes we can declare a class inside another class, such type of classes are called inner classes.  
Without existing one type of object if there is no chance of existing another type of object, then we should go for inner classes.  

```
class Person:
    def __init__(self,name,day,month,year):
        self.name=name
        self.db=self.Dob(day,month,year)
    def display(self):
        print('Name:',self.name)
    class Dob:
        def __init__(self,day,month,year):
            self.dd=day
            self.mm=month
            self.yy=year
        def display(self):
            print('Dob={}/{}/{}'.format(self.dd,self.mm,self.yy))
p=Person("munikumar",1,1,2000)
p.display()
x=p.db
x.display()
```
**Garbage collector**  
main objective of Garbage Collector is to destroy useless objects.  
If an object does not have any reference variable then that object eligible for Garbage Collection.  
1) gc.isenabled() : Returns True if GC enabled  
2) gc.disable() : To disable GC explicitly  
3) gc.enable() : To enable GC explicitly  

**Destructors:**  
Destructor is a special method and the name should be `__del__`  
Just before destroying an object Garbage Collector always calls destructor to perform
clean up activities (Resource deallocation activities like close database connection etc).  
Once destructor execution completed then Garbage Collector automatically destroys
that object.  

```
class Test:
    def __init__(self):
        print("Constructor Execution...")
    def __del__(self):
        print("Destructor Execution...")
test1=Test()
test2=test1
del test1
```
to find the Number of References of an Object:
sys module contains getrefcount() function for this purpose.  
`sys.getrefcount(objectreference)`  
## Inheritance  
What ever variables, methods and constructors available in the parent class by default
available to the child classes and we are not required to rewrite. Hence the main
advantage of inheritance is Code Reusability and we can extend existing functionality
with some more extra functionality.
Types of Inheritance:  
**1) Single Inheritance:**  
The concept of inheriting the properties from one class to another class is known as
single inheritance.  
```
class P:
    def m1(self):
        print("Parent Method")
class C(P):
    def m2(self):
        print("Child Method")
c=C()
c.m1()
c.m2()
```

**2) Multi Level Inheritance:**  
The concept of inheriting the properties from multiple classes to single class with the
concept of one after another is known as multilevel inheritance.  
```
class P:
    def m1(self):
        print("Parent Method")
class C(P):
    def m2(self):
        print("Child Method")
class CC(C):
    def m3(self):
        print("sub child Method")
c=CC()
c.m1()
c.m2()
c.m3()
```
**3) Hierarchical Inheritance:**  
The concept of inheriting properties from one class into multiple classes which are
present at same level is known as Hierarchical Inheritance  
```
class P:
    def m1(self):
        print("Parent Method")
class C1(P):
    def m2(self):
        print("Child1 Method")
class C2(P):
    def m3(self):
        print("Child2 Method")
c1=C1()
c2=C2()
c1.m1()
c2.m1()
c1.m2()
c2.m3()
```

**4) Multiple Inheritance:**  
The concept of inheriting the properties from multiple classes into a single class at a time, is known as multiple inheritance.  

```
class P1:
    def m1(self):
        print("Parent1 Method")
class P2:
    def m2(self):
        print("Parent2 Method")
class C(P1,P2):
    def m3(self):
        print("Child2 Method")
c=C()
c.m1()
c.m2()
c.m3()
```

**5) Hybrid Inheritance:**  
Combination of Single, Multi level, multiple and Hierarchical inheritance is known as Hybrid Inheritance.  
**super() Method:**  
super() is a built-in method which is useful to call the super class constructors, variables and methods from the child class.  