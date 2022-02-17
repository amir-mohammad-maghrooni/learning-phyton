#SETS is a collection which is unordered, unchangeable, and unindexed
#SETS cannot have duplicates in them!
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#duplicate items will be ignored
#can use the len() function to determine the length of SET 
print(len(thisset))
#set items can be of any data
set1 = {"abc", 34, True, 40, "male"}
#It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
print("--------------------------------------------------")
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x);
#or print if item is present in the set
print("------------------------------------")
print("banana" in thisset);
#once a set is created you cannot remove an item from it but you can add to it
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
print("-----------------------------------------------")
#to add items from other sets you can use the update() function
setno1 = {"one","two","three","four"}
setno2 ={"five","six","seven","eight"}

setno1.update(setno2)

print(setno1);#frogot that sets are unorderd -_-
print("--------------------------------------------------------")
#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
print("-------------------------------------------------")
#another way to add sets together is the union() function
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
print("-------------------------------------------")
#The intersection_update() method will keep only the items that are present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
print("-------------------------------------------------")
#The intersection() method will return a new set, that only contains the items that are present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
print("---------------------------------------------")
#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
print("---------------------------------------------")
#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
print("--------------------------------------")
"""
Python has a set of built-in methods that you can use on sets.

Method	                            Description
add()	                            Adds an element to the set
clear()	                            Removes all the elements from the set
copy()	                            Returns a copy of the set
difference()	                    Returns a set containing the difference between two or more sets
difference_update()	                Removes the items in this set that are also included in another, specified set
discard()	                        Remove the specified item
intersection()	                    Returns a set, that is the intersection of two other sets
intersection_update()	            Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                    Returns whether two sets have a intersection or not
issubset()	                        Returns whether another set contains this set or not
issuperset()	                    Returns whether this set contains another set or not
pop()	                            Removes an element from the set
remove()	                        Removes the specified element
symmetric_difference()	            Returns a set with the symmetric differences of two sets
symmetric_difference_update()	    inserts the symmetric differences from this set and another
union()	                            Return a set containing the union of sets
update()	                        Update the set with the union of this set and others
"""
