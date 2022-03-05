#Dictionaries!
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#Dictionaries are used to store data values in key:value pairs.
#dictionaries are ordered and changable but do not allow duplicates
print("-----------------")
#you can use the key name in key:value of dictionaries to print a specefic item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
print("--------------------------")
#Dictionaries cannot have two items with the same key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print("------------------------------------")
#you can use the len() function to determine the length of the dictionaries
print(len(thisdict));
#and dictionaries also support all types of data
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print("----------------------------------------");
#You can access the items of a dictionary by referring to its key name, inside square brackets [] [] []
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x);
y = thisdict.get("model")
print(y);
print("------------------------------------------------")
#The keys() method will return a list of all the keys in the dictionary
#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
print("---------------------------------------")
#The values() method will return a list of all the values in the dictionary
#The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
print("----------------------------------------------")
#The items() method will return each item in a dictionary, as tuples in a list
#The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
print("----------------------------------------------------")
#to find out if a key is in a dictionary you can use th in keyword
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
print("------------------------------")
#You can change the value of a specific item by referring to its key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict["year"] = 2018
print(thisdict)
print("------------------------------------------------")
#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.update({"year": 2020}) #it will also add the key:value if it does not exist
print(thisdict);
print("----------------------------------")
#Adding an item to the dictionary is done by using a new index key and assigning a value to it
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
print("----------------------------------------")
"""
There are several methods to remove items from a dictionary
The pop() method removes the item with the specified key name
The popitem() method removes the last inserted item
The del keyword removes the item with the specified key name
!!!The del keyword can also delete the dictionary completely!!!
The clear() method empties the dictionary
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model") #the pop() method removes the specific item with the key name
print(thisdict)
print("------------------------------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem() #the popitem() method removes the last inserted item - which in this dict it is the year
print(thisdict)
print("-----------------------------------------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["brand"] #the del keyword will remove the specific key name - if used without specifying the key name (del thisdict ) it will remove the whole dict
print(thisdict)
print("--------------------------")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear() #this will empty out the dict
print(thisdict)
print("---------------------------------")
#You can loop through a dictionary by using a for loop.
#When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x) #prints all of the keys one by one
print("||||||||||||||")
for x in thisdict:
  print(thisdict[x]) #prints all values in the dict
print("||||||||||||||")
#You can also use the values() method to return values of a dictionary
for x in thisdict.values():
  print(x)
print("||||||||||||||")
#You can use the keys() method to return the keys of a dictionary
for x in thisdict.keys():
  print(x)
print("||||||||||||||")
#Loop through both keys and values, by using the items() method
for x, y in thisdict.items():
  print(x, y)
print("||||||||||||||")
#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2
#insted you use the copy() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
print("---------------------")
#Another way to make a copy is to use the built-in function dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
print("-------------------------")
#A dictionary can contain dictionaries, this is called nested dictionaries.

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily);
print("-----------------------------------")
#Or, if you want to add three dictionaries into a new dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
print("----------------------------------------")
print("||||||||||||||||||||||||||||||||||||||||")
"""
Python has a set of built-in methods that you can use on dictionaries.

Method	        Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
"""