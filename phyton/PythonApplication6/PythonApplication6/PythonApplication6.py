#Tuples
#its like list but its orderd and unchangable
thistuple =("apple","banana","cherry");
print(thistuple)
#it also allows duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple);
print(len(thistuple));#len() to determin the length
#for a tuple with one item a comma is needed
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#tuple can store any types of data
tuple1 = ("abc", 34, True, 40, "male")
#you cannot change a tuple once it is created but there is a workaround by making it a list and after the change making it a tuple again
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x);
#to append() or remove() you will need to use this workaround aswell
#but you can add tuples to tuples
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
print("---------------------------------------------------------")
#unpacking a tuple(?)
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red);
print("------");
#if the number of variables are less then values you have to use asterisk* wich adds the rest of the tuple to that variable
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red);
print("------");
