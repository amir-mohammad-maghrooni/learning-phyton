#python iterators & iterables
"""
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__()
"""

#list tuples dictionaries and sets are all iterable objects, they are iterable containers which 

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple) # so basicly it list all of the items in the list/tuple/dict/sets

print(next(myit))#and this calls the item one by one
print(next(myit))
print(next(myit))
print("------------------------------------")

#strings are also iterable
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print("-----------------------------------")

mytuple = ("apple", "banana", "cherry")

for x in mytuple: #We can also use a for loop to iterate through an iterable object
  print(x)#it basicly creates the iter() atomaticly and does the same thing

print("--------------------------------------------------------")

mystr = "banana"

for x in mystr:
  print(x)

print("---------------------------------------------------------")
"""
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.

The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.

The __next__() method also allows you to do operations, and must return the next item in the sequence
"""

class Mynumbers():
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x=self.a
        self.a += 1
        return x

myclass = Mynumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print("---------------------------------------------")

class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumber()
myiter = iter(myclass)

#print(x for x in myiter) seems like this is wrong ... it shows error <generator object <genexpr> at 0x14f9f5fb69e0>
for x in myiter:
    print(x)

print("----------------------------------------------")

#module`s
"""
What is a Module?
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application
To create a module just save the code you want in a file with the file extension .py
"""

import mymodule

mymodule.greeting("jonathan")

print("---------------------------------------------")

import mymodule1 #modules can contain variables of all types

a = mymodule1.person1["age"]
print(a)

print("-----------------------------------------------------")

import mymodule1 as mx #by using (as) after importing the module you can rename it and put a simpler name on it in to use

a = mx.person1["age"]
print(a)

print("----------------------------------------------")

import platform

x = platform.system()
print(x)

print("-----------------------")

import platform

x = dir(platform) #the dir() function shows all of the function names ore variable names in a module
print(x)

print("-----------------------------------------")

from mymodule2 import person1 # you can use the form keyword to only import a part of a module

print(person1["age"]) 

print("------------------------")
#date and time is not a data type in python so there is a module for it named datetime

import datetime

x = datetime.datetime.now() #in this form it contains year month day hour minute and second
print(x)
print("------------------------------")
#you can also create a date time for python to show

x= datetime.datetime(2001, 3, 13)

print(x)

print("------------------------")
#the strftime() method is a formatting method to put the date objects in a readable format

x= datetime.datetime(2001, 3, 13)

print(x)
print(x.strftime("%A"))
"""
A reference of all the legal format codes

%a	Weekday,                            short version	Wed	
%A	Weekday,                            full version	Wednesday	
%w	Weekday as a number 0-6,            0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name,                         short version	Dec	
%B	Month name,                         full version	December	
%m	Month                               as a number 01-12	12	
%y	Year, short version,                without century	18	
%Y	Year,                               full version	2018	
%H	Hour                                00-23	17	
%I	Hour                                00-12	05	
%p	AM/PM	                            PM	
%M	Minute                              00-59	41	
%S	Second                              00-59	08	
%f	Microsecond                         000000-999999	548513	
%z	UTC offset	                        +0100	
%Z	Timezone	                        CST	
%j	Day number of year                  001-366	365	
%U	Week number of year,                Sunday as the first day of week, 00-53	52	
%W	Week number of year,                Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	                            20	
%x	Local version of date	            12/31/18	
%X	Local version of time	            17:41:00	
%%	A % character	%	
%G	ISO 8601                            year	2018	
%u	ISO 8601                            weekday (1-7)	1	
%V	ISO 8601                            weeknumber (01-53)	01
"""


print("------------------------------")
