#boolean is either True or False
print (10 > 9)
print (10 == 9)
print (10 < 9)

a=220
A=33

if A > a:
    print ("A is grater then a")
else:
    print ("A is not grater then a")

print (bool("hello")) #?
print (bool(15)) #?

x= "hello"
X= 15
print (bool(x))
print (bool(X))

"""
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones
"""

#these are are false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#items defined as 0 in classes show false in bool as well
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#defines in functions can also return boolean
def myFunction() :
  return True

if myFunction() :
    print ("YES")
else :
    print ("NO")

#there are other build-in function that willl also return boolean like:
S=300
s="Hi"
print(isinstance(S,int))
print(isinstance(s,int))
print(isinstance(s,str))

print("-------------------------------------------------------------------------------------")

"""
used in numbers
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	same as x*x*x*x*x (the x continues by the number of y)
//	Floor division	x // y  round the devided number to the nearest number (2//15 = 7)

used on variables
opr     example     same as
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

used to compare
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y

used for conditions
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	    Returns True if one of the statements is true	x < 5 or x < 4	
not	    Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

also used for compare (like if both of them are the same or arent the same)
is 	    Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y

used to see if sequence is present or not
in 	    Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y

used to compare binary numbers
& 	AND	    Sets each bit to 1 if both bits are 1
|	OR	    Sets each bit to 1 if one of two bits is 1
 ^	XOR	    Sets each bit to 1 if only one of two bits is 1
~ 	NOT	    Inverts all the bits
<<	Zerofill left shift	    Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""
#cant use Aa Xx Ss

q=300
b=250
d="phyton is one of the simplest yet hardest language"
z=20
c=10
v=529
Q=42.21
B=908.9099
C=20

print ("what is q*z equals to?") , print(q*z)
print(d) , print("is \'yet\' in the statement above?") , print ("yet" in d) , print("is \'control\' in the statement above?") , print ("control" in d)
print ("are z & C equal?") , print (z==C)
print ("what is v minus b?" , v-b)
print ("the variable Q is int" , Q is int)
print ("when we murge Q & B togheter we get :" , Q+B)
if q+b < Q :
    print("q&b compined are grater then Q")
else :
    print("Q was always the grater one")
print("what if C times z plus q plus b minus v times Q mines B devided by c ?" , c*z+q+b-v*Q-B/c , "the pc calc shows somthing diffrent . . . . . ")
