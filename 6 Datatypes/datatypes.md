1. Numeric Types
Python has three primary numeric data types:

int: Represents integers (whole numbers). It can store both positive and negative numbers without any size limit.

python
Copy code
x = 5
y = -10
float: Represents floating-point numbers (numbers with decimal points).

python
Copy code
x = 3.14
y = -0.001
complex: Represents complex numbers (numbers with a real and imaginary part).

python
z = 2 + 3j

2. Text Type
str: Represents a sequence of characters (text). Strings are immutable in Python.
python
s = "Hello, World!"

3. Sequence Types
These types represent ordered collections of items.

list: A mutable sequence, meaning the items can be changed or updated. Lists can contain mixed data types.

python
my_list = [1, 2, 3, "four", 5.0]

tuple: An immutable sequence, meaning its items cannot be changed once defined.

python
my_tuple = (1, 2, 3, "four")
range: Represents a sequence of numbers, typically used in loops.

python

r = range(5)  # This is a sequence of numbers 0 to 4.


4. Set Types
Sets represent unordered collections of unique elements.

set: An unordered collection of unique, immutable elements.

python

my_set = {1, 2, 3, 4}
frozenset: Similar to set, but immutable (you cannot add or remove elements).

python

my_frozenset = frozenset([1, 2, 3])
5. Mapping Type
dict: Represents a collection of key-value pairs. Dictionaries are mutable, and keys must be unique and hashable.
python

my_dict = {"name": "Alice", "age": 30}
6. Boolean Type
bool: Represents True or False values. It's a subclass of int, where True is equal to 1 and False is equal to 
is_active = True
has_failed = False
7. Binary Types
These types represent binary data.

bytes: An immutable sequence of bytes.

python

b = b"hello"
bytearray: A mutable sequence of bytes.

python

ba = bytearray(5)
memoryview: Provides a view of the memory of an object (without copying it), typically used with bytes or bytearray objects.

python
mv = memoryview(b"hello")
8. None Type
NoneType: Represents the absence of a value. In Python, the only instance of NoneType is None.
python

result = None
9. Callable Types
function: Represents a user-defined or built-in function.

python
def my_function():
    return "Hello"
lambda: Represents an anonymous (nameless) function.
my_lambda = lambda x: x * 2
10. Iterator and Generator Types
iterator: An object that can be iterated upon (e.g., a list or tuple). It implements the __iter__() and __next__() methods.

python
it = iter([1, 2, 3])
generator: A type of iterator, defined with a function that uses the yield statement.

python
Copy code
def my_generator():
    yield 1
    yield 2
11. Custom Object Types
In Python, you can also define your own data types by creating classes:

python
Copy code
class MyClass:
    pass

obj = MyClass()
Type Checking
To check the type of an object, you can use the type() function:

python
print(type(5))  # Output: <class 'int'>
You can also check if an object is an instance of a specific type using isinstance():

python
print(isinstance(5, int))  # Out