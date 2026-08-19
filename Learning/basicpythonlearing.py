# ==========================================================
# PYTHON TUTORIAL - FULL NOTES
# ==========================================================


# ----------------------------------------------------------
# Python HOME
# ----------------------------------------------------------
# Python is a popular, high-level, general-purpose programming
# language used for web development, automation, data science,
# AI, scripting, and more.

# ----------------------------------------------------------
# Python Intro
# ----------------------------------------------------------
# Python was created by Guido van Rossum, released in 1991.
# It is interpreted, dynamically typed, and easy to read.
print("Hello from Python Intro")


# ----------------------------------------------------------
# Python Get Started
# ----------------------------------------------------------
# Run python files using: python filename.py
print("Hello, World!")


# ----------------------------------------------------------
# Python Syntax
# ----------------------------------------------------------
# Python uses indentation (whitespace) to define code blocks.
if 5 > 2:
    print("Five is greater than two!")  # indented block


# ----------------------------------------------------------
# Python Output
# ----------------------------------------------------------
print("Hello, World!")
print("Hello", "World", sep=", ")   # multiple values
print("Line1", end=" - ")
print("Line2")


# ----------------------------------------------------------
# Python Comments
# ----------------------------------------------------------
# This is a single line comment
"""
This is a
multiline comment (docstring style)
"""
print("Comments example")  # inline comment


# ----------------------------------------------------------
# Python Variables
# ----------------------------------------------------------
x = 5
y = "John"
print(x)
print(y)

x, y, z = 1, 2, 3   # multiple assignment
print(x, y, z)

x = y = z = "Same"  # same value to multiple variables
print(x, y, z)


# ----------------------------------------------------------
# Python Data Types
# ----------------------------------------------------------
a = 5             # int
b = 5.5           # float
c = "hello"       # str
d = True          # bool
e = [1, 2, 3]     # list
f = (1, 2, 3)     # tuple
g = {1, 2, 3}     # set
h = {"key": "val"}  # dict
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h))


# ----------------------------------------------------------
# Python Numbers
# ----------------------------------------------------------
x = 1        # int
y = 2.8      # float
z = 1j       # complex
print(type(x), type(y), type(z))
print(x + y)  # int + float = float


# ----------------------------------------------------------
# Python Casting
# ----------------------------------------------------------
x = int(1)      # x will be 1
y = int(2.8)     # y will be 2
z = int("3")     # z will be 3
a = float("4.2") # a will be 4.2
b = str(5)       # b will be '5'
print(x, y, z, a, b)


# ----------------------------------------------------------
# Python Strings
# ----------------------------------------------------------
s = "Hello, World!"
print(s[1])           # indexing
print(s[2:5])          # slicing
print(len(s))           # length
print(s.upper())
print(s.lower())
print(s.strip())
print(s.replace("H", "J"))
print(s.split(","))
print("Hello" in s)     # check substring
print(s[::-1])           # reverse string


# ----------------------------------------------------------
# Python Booleans
# ----------------------------------------------------------
print(10 > 9)     # True
print(10 == 9)    # False
print(bool("hello"))  # True
print(bool(0))         # False


# ----------------------------------------------------------
# Python Operators
# ----------------------------------------------------------
print(5 + 3)    # arithmetic
print(5 == 3)   # comparison
print(5 > 3 and 3 > 1)  # logical
x = 5
x += 3          # assignment operator
print(x)
print(5 in [1, 2, 5])   # membership
print(5 is 5)             # identity


# ----------------------------------------------------------
# Python Lists
# ----------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits.append("orange")
fruits.insert(1, "mango")
fruits.remove("banana")
fruits.sort()
print(fruits)
print(len(fruits))
for f in fruits:
    print(f)


# ----------------------------------------------------------
# Python Tuples
# ----------------------------------------------------------
t = ("apple", "banana", "cherry")
print(t[0])
print(len(t))
# tuples are immutable, but can be converted to list to change
y = list(t)
y.append("orange")
t = tuple(y)
print(t)


# ----------------------------------------------------------
# Python Sets
# ----------------------------------------------------------
s = {"apple", "banana", "cherry"}
s.add("orange")
s.remove("banana")
print(s)
s2 = {"banana", "kiwi"}
print(s.union(s2))
print(s.intersection(s2))


# ----------------------------------------------------------
# Python Dictionaries
# ----------------------------------------------------------
d = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(d["brand"])
d["year"] = 2020
d["color"] = "red"
print(d)
for key, value in d.items():
    print(key, value)
print(d.keys())
print(d.values())


# ----------------------------------------------------------
# Python If...Else
# ----------------------------------------------------------
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

print("A") if a > b else print("B")  # short hand if else


# ----------------------------------------------------------
# Python Match
# ----------------------------------------------------------
day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 4:
        print("Thursday")
    case _:
        print("Another day")


# ----------------------------------------------------------
# Python While Loops
# ----------------------------------------------------------
i = 1
while i < 6:
    print(i)
    if i == 3:
        pass  # placeholder
    i += 1
else:
    print("i is no longer less than 6")


# ----------------------------------------------------------
# Python For Loops
# ----------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    if f == "banana":
        continue
    print(f)

for x in range(6):
    if x == 4:
        break
    print(x)


# ----------------------------------------------------------
# Python Functions
# ----------------------------------------------------------
def my_function(fname, lname="Doe"):  # default parameter
    print(fname + " " + lname)

my_function("Emil")

def my_function2(*kids):   # arbitrary arguments
    print("The youngest child is " + kids[-1])

my_function2("Emil", "Tobias", "Linus")

def my_function3(**kid):   # arbitrary keyword arguments
    print("His last name is " + kid["lname"])

my_function3(fname="Tobias", lname="Refsnes")

def square(x):
    return x * x

print(square(5))


# ----------------------------------------------------------
# Python Range
# ----------------------------------------------------------
for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):  # start, stop, step
    print(x)


# ----------------------------------------------------------
# Python Arrays
# ----------------------------------------------------------
import array
cars = array.array('i', [1, 2, 3])   # typed array (i = integer)
print(cars[0])
cars.append(4)
print(cars)
print(len(cars))
# Note: Python's built-in list is more commonly used as an "array"


# ----------------------------------------------------------
# Python Iterators
# ----------------------------------------------------------
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))


# ----------------------------------------------------------
# Python Modules
# ----------------------------------------------------------
# save code in mymodule.py, then import it:
# import mymodule
# mymodule.greeting("Jonathan")
import platform
print(platform.system())   # using a built-in module

from platform import system  # import specific part
print(system())

print(dir(platform))  # list all names in a module


# ----------------------------------------------------------
# Python Dates
# ----------------------------------------------------------
import datetime
x = datetime.datetime.now()
print(x)
print(x.year, x.strftime("%A"))  # weekday name

x = datetime.datetime(2020, 5, 17)  # create specific date
print(x)
print(x.strftime("%B %d, %Y"))   # formatted output


# ----------------------------------------------------------
# Python Math
# ----------------------------------------------------------
import math
print(math.sqrt(64))
print(math.ceil(1.4))
print(math.floor(1.4))
print(math.pi)
print(min(5, 10, 25))
print(max(5, 10, 25))
print(abs(-7.25))
print(pow(4, 3))


# ----------------------------------------------------------
# Python JSON
# ----------------------------------------------------------
import json
x = '{"name": "John", "age": 30, "city": "New York"}'
y = json.loads(x)   # JSON to Python
print(y["age"])

person = {"name": "John", "age": 30}
z = json.dumps(person)  # Python to JSON
print(z)

print(json.dumps(person, indent=4))  # pretty print


# ----------------------------------------------------------
# Python RegEx
# ----------------------------------------------------------
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)  # check if pattern matches
print(bool(x))

x = re.findall("ai", txt)  # find all matches
print(x)

x = re.split("\\s", txt)   # split at whitespace
print(x)

x = re.sub("\\s", "-", txt)  # replace whitespace with -
print(x)


# ----------------------------------------------------------
# Python PIP
# ----------------------------------------------------------
# PIP is the package manager for Python.
# Install a package:      pip install camelcase
# List installed packages: pip list
# Remove a package:       pip uninstall camelcase
# Example usage after installing:
# import camelcase
# c = camelcase.CamelCase()
# print(c.hump("hello world"))


# ----------------------------------------------------------
# Python Try...Except
# ----------------------------------------------------------
try:
    print(x_not_defined)
except NameError:
    print("Variable x is not defined")
except Exception:
    print("Something else went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")

try:
    raise Exception("A custom error occurred")  # raise an exception
except Exception as e:
    print(e)


# ----------------------------------------------------------
# Python String Formatting
# ----------------------------------------------------------
age = 36
txt = f"My name is John, I am {age}"   # f-string
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"  # format number
print(txt)

txt2 = "My name is {}, I am {}".format("John", 36)  # .format()
print(txt2)


# ----------------------------------------------------------
# Python None
# ----------------------------------------------------------
x = None
print(x)
print(type(x))
if x is None:
    print("x has no value")


# ----------------------------------------------------------
# Python User Input
# ----------------------------------------------------------
# username = input("Enter username:")
# print("Username is: " + username)
print("User input example (commented out for script execution)")


# ----------------------------------------------------------
# Python VirtualEnv
# ----------------------------------------------------------
# Create a virtual environment:
#   python -m venv myenv
# Activate it:
#   Windows: myenv\\Scripts\\activate
#   Mac/Linux: source myenv/bin/activate
# Install packages inside venv:
#   pip install requests
# Deactivate:
#   deactivate


# ==========================================================
# PYTHON CLASSES
# ==========================================================

# ----------------------------------------------------------
# Python OOP
# ----------------------------------------------------------
# OOP organizes code using objects that contain data (attributes)
# and code (methods). Core concepts: Class, Object, Inheritance,
# Polymorphism, Encapsulation, Abstraction.

# ----------------------------------------------------------
# Python Classes/Objects
# ----------------------------------------------------------
class MyClass:
    x = 5

p1 = MyClass()   # create an object
print(p1.x)


# ----------------------------------------------------------
# Python __init__ Method
# ----------------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name, p1.age)


# ----------------------------------------------------------
# Python self Parameter
# ----------------------------------------------------------
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person2("John", 36)
p1.myfunc()   # self refers to the current instance


# ----------------------------------------------------------
# Python Class Properties
# ----------------------------------------------------------
class Person3:
    def __init__(self, name, age):
        self.name = name  # property
        self.age = age    # property

p1 = Person3("John", 36)
print(p1.name)
p1.age = 40   # modify property
print(p1.age)
del p1.age    # delete property
# print(p1.age)  # would raise AttributeError


# ----------------------------------------------------------
# Python Class Methods
# ----------------------------------------------------------
class Person4:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person4("John", 36)
p1.myfunc()   # calling a method on the object


# ----------------------------------------------------------
# Python Inheritance
# ----------------------------------------------------------
class Student(Person):   # inherits from Person defined above
    def __init__(self, name, age, graduationyear):
        super().__init__(name, age)  # call parent constructor
        self.graduationyear = graduationyear
    def welcome(self):
        print("Welcome", self.name, "to the class of", self.graduationyear)

s1 = Student("Mike", 20, 2024)
s1.welcome()


# ----------------------------------------------------------
# Python Polymorphism
# ----------------------------------------------------------
class Car:
    def move(self):
        print("Drive!")

class Boat:
    def move(self):
        print("Sail!")

class Plane:
    def move(self):
        print("Fly!")

for vehicle in (Car(), Boat(), Plane()):
    vehicle.move()   # same method name, different behavior


# ----------------------------------------------------------
# Python Encapsulation
# ----------------------------------------------------------
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private attribute (double underscore)
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance

acc = BankAccount(100)
acc.deposit(50)
print(acc.get_balance())   # access via method, not directly


# ----------------------------------------------------------
# Python Inner Classes
# ----------------------------------------------------------
class Outer:
    def __init__(self):
        self.name = "Outer class"
        self.inner = self.Inner()   # instantiate inner class

    class Inner:
        def __init__(self):
            self.name = "Inner class"

outer_obj = Outer()
print(outer_obj.name)
print(outer_obj.inner.name)


# ==========================================================
# FILE HANDLING
# ==========================================================

# ----------------------------------------------------------
# Python File Handling
# ----------------------------------------------------------
# Key functions: open(), read(), write(), close()
# Modes: "r" read, "a" append, "w" write, "x" create
# "t" text mode (default), "b" binary mode

# ----------------------------------------------------------
# Python Read Files
# ----------------------------------------------------------
with open("demofile.txt", "w") as f:   # create file first for demo
    f.write("Hello! Welcome to demofile.txt")

f = open("demofile.txt", "r")
print(f.read())        # read whole file
f.close()

f = open("demofile.txt", "r")
print(f.readline())    # read one line
f.close()

with open("demofile.txt", "r") as f:   # using "with" (auto closes)
    for line in f:
        print(line)


# ----------------------------------------------------------
# Python Write/Create Files
# ----------------------------------------------------------
f = open("demofile2.txt", "w")   # "w" overwrite/create
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile2.txt", "a")   # "a" append
f.write(" This is added text.")
f.close()

f = open("demofile2.txt", "r")
print(f.read())
f.close()

f = open("newfile.txt", "x")   # "x" create (error if exists)
f.close()


# ----------------------------------------------------------
# Python Delete Files
# ----------------------------------------------------------
import os
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")     # delete a file
else:
    print("The file does not exist")

# to delete a folder:
# os.rmdir("myfolder")

# check before deleting
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
    print("demofile.txt deleted")


# ==========================================================
# EXTRA TOPICS (BONUS - not in original list)
# ==========================================================

# ----------------------------------------------------------
# Python Scope
# ----------------------------------------------------------
x = 300   # global variable

def myfunc():
    x = 200   # local variable (only exists inside function)
    print(x)

myfunc()
print(x)   # prints global x, unaffected by local x

def myfunc2():
    x = 100
    def myinnerfunc():
        print(x)   # inner function can access outer function's variable
    myinnerfunc()

myfunc2()


# ----------------------------------------------------------
# Python Global Keyword
# ----------------------------------------------------------
def myfunc3():
    global x
    x = 300   # creates/modifies a global variable from inside function

myfunc3()
print(x)

x = 300
def myfunc4():
    global x
    x = 200   # global keyword lets us change the global value here
myfunc4()
print(x)


# ----------------------------------------------------------
# Python Lambda
# ----------------------------------------------------------
x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b   # multiple arguments
print(x(5, 6))

def myfunc5(n):
    return lambda a: a * n   # lambda inside a function

doubler = myfunc5(2)
print(doubler(11))

points = [(1, 2), (3, 1), (5, 0)]
points.sort(key=lambda p: p[1])   # lambda as sort key
print(points)


# ----------------------------------------------------------
# Python Recursion
# ----------------------------------------------------------
def factorial(n):
    if n <= 1:      # base case
        return 1
    return n * factorial(n - 1)   # recursive call

print(factorial(5))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(7):
    print(fibonacci(i), end=" ")
print()


# ----------------------------------------------------------
# Python Multiple Inheritance
# ----------------------------------------------------------
class Father:
    def skills(self):
        print("Gardening, Cooking")

class Mother:
    def hobbies(self):
        print("Painting, Dancing")

class Child(Father, Mother):   # inherits from multiple parent classes
    def show(self):
        print("I inherit skills from both parents")

c = Child()
c.skills()
c.hobbies()
c.show()

print(Child.__mro__)   # method resolution order


# ----------------------------------------------------------
# Python Constructor
# ----------------------------------------------------------
# The constructor is the __init__ method, automatically called
# when a new object is created. It initializes the object's state.
class Employee:
    def __init__(self, name, salary):
        print("Constructor called: creating Employee object")
        self.name = name
        self.salary = salary
    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

e1 = Employee("Alice", 50000)   # __init__ runs automatically here
e1.display()

# constructor with default values
class Employee2:
    def __init__(self, name="Unknown", salary=0):
        self.name = name
        self.salary = salary

e2 = Employee2()
e2.display = lambda: print(e2.name, e2.salary)
e2.display()


# ----------------------------------------------------------
# Python Destructor
# ----------------------------------------------------------
# The destructor is the __del__ method, automatically called
# when an object is about to be destroyed (garbage collected).
class Employee3:
    def __init__(self, name):
        self.name = name
        print(f"Constructor: {self.name} object created")
    def __del__(self):
        print(f"Destructor: {self.name} object destroyed")

e3 = Employee3("Bob")
del e3   # explicitly deletes the object, triggers __del__

# Note: __del__ is also called automatically when the program ends
# or when the object has no more references (garbage collection).


# ==========================================================
# END OF NOTES
# ==========================================================