import random
print("Hello world")
x = 5
y = "John"
print(x)
print(y)

# write comment
print("Hello, World!")
"""
roaa abushaqrah
"""
# declear variable
# start
x = "roaa.t. abu-shaqrah"
print(x)

x = str(3)
print(x)
y = int(3)
print(y)
z = float(3)
print(z)
# End variable topics
# Get the Type
x = 5
y = "roaa"
print(type(x))
print(type(y))
# End Get the Type
# varibleName
myvar = "orange"
print(myvar)
_myvar = "code"
print(_myvar)
myVar = 'r'
print(myVar)
MYVAR = "coding academy"
print(MYVAR)

# Snake Case
#my_variable_name = "John"

# Pascal Case
#MyVariableName = "John"

# Many Values to Multiple Variables
x, z, y = 5, 8, 9
print(x)
print(y)
print(z)
# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
# Unpack a Collection
fruit = ['apple', 'banana']
x, y = fruit
print(x)
print(y)
# Output Variables
x = "abushaqrah"
print("Roaa " + x)

# Global Variables
x = "assel"

""""
def myfun():


print(x)

myfun()

"""
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)
# data type complex
x = 1j
print(type(x))
# tuple
x = ("apple", "banana", "cherry")
print(x)
print(type(x))

# range
x = range(8)
print(x)
# disc
x = {"name": "John", "age": 36}
print(x)
# frozenset
x = frozenset({"apple", "banana", "cherry"})

print(x)

# Convert from one type to another:
x = 1
a = float(x)
print(type(a))

# Random Number


print(random.randrange(1, 10))

# Specify a Variable Type
# INT
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

# float
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)
# string
x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)
# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Looping Through a String
for x in "banana":
    print(x)

    # String Length

a = "Hello, World!"
print(len(a))
# Check String
txt = "The best things in life are free!"
print("free" in txt)
# useif
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)
# print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")


# Python - Slicing Strings
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
b = "Hello, World!"
print(b[:5])

# Slice To the End
b = "Hello, World!"
print(b[2:])
# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])
# Upper Case
a = "Hello, World!"
print(a.upper())
# Lower Case
a = "Hello, World!"
print(a.lower())
# Remove Whitespace
a = " Hello, World! "
print(a.strip())

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))
# Split String
a = "Hello, World!"
print(a.split(","))

# String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c)
# To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)
# String Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# string
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
