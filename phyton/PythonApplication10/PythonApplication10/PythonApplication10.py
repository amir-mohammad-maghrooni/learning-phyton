"""
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result
"""
def my_function():#to create a function use the def keyword
    print("Hello from a function")

my_function();#to call a function just use the name used in creating the function

print("----------------------------------------------")

def my_function(fname):#Information can be passed into functions as arguments
  print(fname + " Refsnes")
#Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma
my_function("Emil")
my_function("Tobias")
my_function("Linus")

print("---------------------------------------------------")

def my_function(*kids):#if you do not know how many arguments will be passed on use a * before the parameter name in the function def
  print("The youngest child is " + kids[2])#this way the function will receve a tuple of arguments

my_function("Emil", "Tobias", "Linus")

print("-------------------------------------------------")

#You can also send arguments with the key = value syntax *This way the order of the arguments does not matter*

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

print("---------------------------------------------------")

#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition

def my_function(**kid):
  print("His last name is " + kid["lname"])#This way the function will receive a dictionary of arguments, and can access the items accordingly

my_function(fname = "Tobias", lname = "Refsnes")

print("----------------------------------------------------")

def my_function(country = "Iran"):#like this we can set a default parameter value
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()#when we call an empty argument it will use the default value we set
my_function("Brazil")

print("------------------------------------------------------")

def my_function(x):
  return 5 * x #To let a function return a value, use the return statement

print(my_function(3))
print(my_function(5))
print(my_function(9))
print(my_function(39))

print("-------------------------------------------------------")
"""
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
"""
def tri_recursion(k): 
  if(k > 0): #the rule
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0 # the kill switch / stop switch
  return result

print("\n\nRecursion Example Results")
tri_recursion(6) #this number is K

print("-----------------------------------------------------")

#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression

x = lambda a : a + 10 #the expression is the end result wich is returned
print(x(5))

print("--------------------------------------------------------")

x = lambda a, b : a * b
print(x(5, 6))
print("-----------")
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

print("-------------------------------------------------------")

#The power of lambda is better shown when you use them as an anonymous function inside another function

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) #will double any number 

print(mydoubler(11)) # this number will be doubled 

print("----------")

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

print("-----------------------------------------------------------")

