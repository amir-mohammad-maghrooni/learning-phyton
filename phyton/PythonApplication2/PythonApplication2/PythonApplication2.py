x = " is awsome"
z="mark"

def myfunc():
    x= " is simple"
    print ("phyton" + x)
    global z
    z="marketing"

myfunc()

print("phyton"+x)
print(z + "is difficult")
"""
# variable types:
text = str
numeric = int , float , complex
sequence? = list , tuple , range
mapping? =  dict
set = set , frozenset
boolean= bool
binary= bytes , bytearray , memoryview
"""
a = "Hello World"	#str	
A = 20	#int	
b = 20.5	#float	
B = 1j	#complex	
c = ["apple", "banana", "cherry"]	#list	
C = ("apple", "banana", "cherry")	#tuple	
d = range(6)	#range	
D = {"name" : "John", "age" : 36}	#dict	
e = {"apple", "banana", "cherry"}	#set	
E = frozenset({"apple", "banana", "cherry"})	#frozenset	
f = True	#bool	
F = b"Hello"	#bytes	
g = bytearray(5)	#bytearray	
G = memoryview(bytes(5))	#memoryview	
print(a) , print(type(a))
print(A) , print(type(A))
print(b) , print(type(b))
print(B) , print(type(B))
print(c) , print(type(c))
print(C) , print(type(C))
print(d) , print(type(d))
print(D) , print(type(D))
print(e) , print(type(e))
print(E) , print(type(E))
print(f) , print(type(f))
print(F) , print(type(F))
print(g) , print(type(g))
print(G) , print(type(G))

#can also be typed like this
#x = str('Hello World')	str	
#x = int(20)	int	
#x = float(20.5)	float	
#x = complex(1j)	complex	
#x = list(('apple', 'banana', 'cherry'))	list	
#x = tuple(('apple', 'banana', 'cherry'))	tuple	
#x = range(6)	range	
#x = dict(name='John', age=36)	dict	
#x = set(('apple', 'banana', 'cherry'))	set	
#x = frozenset(('apple', 'banana', 'cherry'))	frozenset	
#x = bool(5)	bool	
#x = bytes(5)	bytes	
#x = bytearray(5)	bytearray	
#x = memoryview(bytes(5))	memoryview


import random
print (random.randrange(1,50))
print (random.randrange(1,50))
print (random.randrange(1,50))
print (random.randrange(1,50))
print (random.randrange(1,50))