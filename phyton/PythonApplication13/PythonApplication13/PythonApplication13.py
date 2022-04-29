#python maths ....
#the built in math functions

x= min(12,23,42,14,51,3,531,53,34,11,4,9) #the min finds and returns the smallest value
y= max(12,23,42,14,51,3,531,53,34,11,4,9) #the max finds and returns the biggest value

print("min=", x)
print("max=", y)

print("-----------------------------------")

x = abs(-7.25) #the abs find and returnd the absolute number or the positive number

print(x)

print("--------------------------------------")

x = pow(4, 3) #the pow() return the value of the first number to the power of the second number or in this case 4*4*4

print(x)

print("---------------------------")
#Python has also a built-in module called math, which extends the list of mathematical functions

import math

x = math.sqrt(64) #the sqrt() will return the square root of the given number

print(x)

print("----------------------------------------------------------")
#The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer

x = math.ceil(1.4)
y = math.floor(1.4)

print(x)#will return 2
print(y)#will retunn 1

print("---------------------------------------")
#The math.pi constant, returns the value of PI (3.14...)

x = math.pi

print(x)

print("-----------------------------------------------------------")
#json
#JSON is a syntax for storing and exchanging data , JSON is text, written with JavaScript object notation
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x) #If you have a JSON string, you can parse it by using the json.loads() method

# the result is a Python dictionary:
print(y["age"])

print("---------------------------------------------------------")

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x) #If you have a Python object, you can convert it into a JSON string by using the json.dumps() method

# the result is a JSON string:
print(y)

print("-----------------------------------------")
#these python objects can be converted into json strings
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

"""
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python	        JSON
dict	        Object
list	        Array
tuple	        Array
str	            String
int	            Number
float	        Number
True	        true
False	        false
None	        null
"""

print("--------------------------")

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

print("---------------------------------------")

#the indent parameter defines the number of indents
#with the separators you can define (",",":") which means using a comma and a space to separate each object and a colon and a space to separate keys frome value

print(json.dumps(x, indent=4, separators=(". "," = ")))
print("------")
print(json.dumps(x, indent=4, sort_keys=True))