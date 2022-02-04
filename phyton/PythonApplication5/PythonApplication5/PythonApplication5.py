
#starting again from oprations . . . . 
#the simplest operation is the + sign
print(10 + 5);
"""
Python Arithmetic Operators
+   Addition    x+y
-   Subtraction     x-y
*   Multiplication  x*y
/   division    x/y
%   modulus(baghimande)     x%y
**  Exponentiation(be tavan resandan)   x**y
// Floor division(rond sazi)    x//y
"""
"""
Python Assignment Operators
=	    x = 5	    x = 5	
+=	    x += 3	    x = x + 3	
-=	    x -= 3	    x = x - 3	
*=	    x *= 3	    x = x * 3	
/=	    x /= 3	    x = x / 3	
%=	    x %= 3	    x = x % 3	
//=	    x //= 3	    x = x // 3	
**=	    x **= 3	    x = x ** 3	
&=	    x &= 3	    x = x & 3	
|=	    x |= 3	    x = x | 3	
^=	    x ^= 3	    x = x ^ 3	
>>=	    x >>= 3	    x = x >> 3	
<<=	    x <<= 3	    x = x << 3
"""
"""
Python Comparison Operators
==	    Equal	    x == y	
!=	    Not equal	    x != y	
>	    Greater than	    x > y	
<	    Less than	    x < y	
>=	    Greater than or equal to	    x >= y	
<=	    Less than or equal to	    x <= y
"""
"""
Python Logical Operators
and 	    Returns True if both statements are true	    x < 5 and  x < 10	
or	    Returns True if one of the statements is true	    x < 5 or x < 4	
not	    Reverse the result, returns False if the result is true	not     (x < 5 and x < 10)

Python Identity Operators
is 	    Returns True if both variables are the same object	    x is y	
is not	    Returns True if both variables are not the same object	    x is not y	

Python Membership Operators
in 	    Returns True if a sequence with the specified value is present in the object	    x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	    x not in y

Python Bitwise Operators
& 	    AND	Sets each bit to 1 if both bits are 1
|	    OR	Sets each bit to 1 if one of two bits is 1
 ^	    XOR	Sets each bit to 1 if only one of two bits is 1
~ 	    NOT	Inverts all the bits
<<	    Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	    Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""
#i better stop copy and pasting things . . . . .
A = 25;
a = 2;
B = 3;
b = 50;
print("the combonation of the integer A and B equals to:\n", A ,"+", B ,"=",A+B);
C = B + A;
print ("The Combined Might Of b & a Equals TO:\n",a,"+",b,"=",a+b);
c = a + b;
print ("and those two make the Lucky people of C & c!\n","small c equals to:",c,"\n and the BIG C equals to:",C,);
print ("-------------------------------------------------------------------------------------------------------------")
#cant use Aa Bb Cc
#And now we enter the wonderfull world of lists
thislist = ["apple","banana","cherry"];
print (thislist);
#lists can store multiple items in a single variable witch are orderds and indexed as [0] & [1] and so on and it can also have duplicate items in it
print (thislist[0]);
print (thislist[1]);
print (thislist[2]);
thislist2 = ["apple", "banana", "cherry", "apple", "cherry"];
print (thislist2);
#len() shows the lenght of an list or determins how many items an list has
print (len(thislist));
print (len(thislist2));
#list can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#or contain many data types
list4 = ["abc", 34, True, 40, "male"]
#type() determins the type or class of the variable
print("the type of a list is:\n",type(thislist),"\nand the type of a,B&c is:\n",type(a),type(B),type(c));
#it is also possible to use the list constructor when creating a new list
thislist3 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist3);
#phyton has four collection arrays
"""
List -- is a collection which is ordered and changeable. Allows duplicate members.
Tuple -- is a collection which is ordered and unchangeable. Allows duplicate members.
Set -- is a collection which is unordered, unchangeable*(still can remove and/or add new items whenever we want), and unindexed. No duplicate members.
Dictionary -- is a collection which is ordered** and changeable. No duplicate members.
"""
#in a list to get the last item you can also use [-1] and for the second last item [-2] etc.
print("with the use of [-1] i can show you the last item of thislist2:\n",thislist2[-1]);
#you can also use [2:5] to specify where the list will start and where it will end
thislist4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist4[2:5])
print(thislist4[:4])
print(thislist4[2:])
print(thislist4[-4:-1])
#note that the first item is [0]
#you can also check if an item is in the list using the in keyword
if "apple" in thislist: 
    print("yes the apple is in the list");
#you can also change the item of the list with a code like before and after or somthing
newlist = ["apple","samsung","huawei","nokia","apple"]
print("the new list of mobile companys are:\n",newlist);
newlist[4]="shiaomi"
print("oops there was a typo in the last list, the new fixed list is this:\n",newlist);
#or you can make ranged changes
newlist2 =["first","second","therd","firth","fith","sixth"]
print (newlist2,"\n this list has some typos in it . . . lets fix it");
newlist2[2:5] =["third","fourth","fifth"]; #writed it as [2:4] at first and it left the fith in
print (newlist2,"\n and now it is fixed");
#you can also add items in lists via the insert() code
newlist2.insert(6,"seventh"); #writed it as a 7 at first . . . stupid mistakes ... frogot that it started from 0 
print(newlist2,"\n and now it has a seventh")
#using append() will add the item at the end of the list
newlist2.append("eighth")
print(newlist2,"\n and now surpise surprise ... it has and eighth number ... and yes eighth is correct not eigth");
newlist3 =["ninth","tenth"]
#by using the extend() code you can use other lists and add it to the desierd list
newlist2.extend(newlist3);
print(newlist2,"\n. . . . . how did the . . . . . did the last two numbers just . . . . suddenly appear?!?");
print("-----------------------------------------------------------");
newlist4 = ["one","two","for","three","four"];
print (newlist4,"\noops there is a problem in this list");
newlist4.remove("for");
print(newlist4,"\nfixed!");
filler1=("five","six","sven")
newlist4.extend(filler1);
print(newlist4,"\n- damn another typo in the list");
newlist4.pop(6)#stupid mistake again . . . writed it as 8 while with the removes it only goes to 6 
#if pop() is not specified it will remove the last item
print(newlist4,"fixed again!");
#there is also the del() command that is the same as pop() but if not specified it will remove the whole list
del newlist4[5];
print(newlist4);
newlist4.clear()#the clear() command clears the list contents and leave the list empty
print(newlist4,"\n the list above is empty!");
print("-----------------------------------------------------------");
#LOOPS
newLiLoop=["one","two","tree","four","five","six","seven","eight"];
for x in newLiLoop:
    print(x);#will print the items in list one by one
print("first example of list looping");
for i in range(len(newLiLoop)):
    print(newLiLoop[1]);# will loop through the list items by referring to their index number
print("second example of list looping");
z=0
while z < len(newLiLoop):
    print(newLiLoop[z]);
    z=z+1;
print("third example of list looping");
#the shortest syntax for list looping
[print(x) for x in newLiLoop];
print("-----------------------------------------------------------");
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
the shortend syntex of the lines above is :
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist5= [x for x in fruits if "a" in x];
print(newlist5,"\n a filterd list of fruits with 'a's in it");
#newlist = [expression for item in iterable if condition == True] "the syntex"
newlist5= [x for x in fruits if x != "apple"];#the condition if is optional
print(newlist5,"\n fruits without apple");
print("---------------------------------------------------------");
newlist6 =["orange", "mango", "kiwi", "pineapple", "banana"]
print(newlist6);
newlist6.sort()#the sort() will sort the list
print(newlist6,"\n two lists unsorted and sorted");
newlist6_1 =[100, 50, 65, 82, 23];
print(newlist6_1)
newlist6_1.sort();
print(newlist6_1);
newlist6.sort(reverse = True)
print(newlist6,"\n the same fruit list reversed sorted!");
#you can also fully reverse the list regardless of the sorting
newlist6 =["orange", "mango", "kiwi", "pineapple", "banana"]
newlist6.reverse();
print(newlist6,"\nreversed!")
print("---------------------------------------")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#the easiest way to join two lists is + 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#or adding them one by one using append()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
#or the extend() command
print("-----------------------------")