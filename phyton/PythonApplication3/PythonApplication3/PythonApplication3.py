x = 1
X = int(1)
#both is correct
a = int(2.8) #will be displayed as 2
A = int("5") #will be displayed as 5
b = float(5) #will be displayed as 5.0
B = float("6.25") #will be displayed as 6.25
c = str(2) #will be displayed as '2'
C = str(3.45) #will be displayed as '3.42'
d = str('s32') #will be displayed as 's32'

print("hello")
print('hello')
#both are the same ' "
D = "can also be applaide to variables"
print(D)
e="""in phyton you can,
do multiline strings,
that can be helpfull"""
print(e)

E="hello world"
print(len(E))

f="hello world"
print(f[4])
txt="the best things in life are free"
print("free"in(txt))
#or

if "free" in txt:
    print('yes "free" is present in txt');

print("expensive" not in(txt))

if "expensive" not in txt:
    print("no 'expensive' is not present in txt")

#slicing is [4:5] two bytes of a string
txt2 = "hello world"
print(txt2 [1:])
print (txt2 [:5])
print (txt2 [-5:-2])

test="test text"
print(test.upper())
print(test.lower())
test2="  test text 2  "
print(test2.strip())
print(test.replace("e","W"))

add1="hello"
add2="world"
add3=add1+add2
print(add3)
add3=add1+" "+add2
print(add3)

#we cannot add numbers to string variables so we use the format method
age=36
text="my name is john, and i am {}"
print(text.format(age))
#format can have unlimited arguments 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity2 = 3
itemno2 = 567
price2 = 49.95
myorder2 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder2.format(quantity2, itemno2, price2))
#for using illigal characters in a statement use \
print ("we are the so called\"vikings\"from the north") #in this statement the viking will be in double qoutes 

#other escape characters are : \' single qouts - \\ back slash - \n new line - \r carrage return (?) - \t tab (?)
#\b backspace - \f froom feed (?)- \ooo octal value (?) - \xhh hex value (?)

print ("we are the so called\'vikings\'from the north") #in this statement the viking will be in single qoutes 
"""
methodes used in "STRING" (str) like <print (txt.upper()) - print (txt.replace ( , ))>
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""