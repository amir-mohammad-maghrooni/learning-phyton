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
