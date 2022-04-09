#classes

class MyClass:
    x =5

p1 = MyClass() #this puts the class into an object
print(p1)

print("------------------------------------------")

class Person:
    def __init__(self, name, age): #__init__ = initiate wich its called atomaticly 
        self.name = name
        self.age = age

p1= Person("mohammad", 22)

print(p1.name)
print(p1.age)

print("-------------------------------------------------")

class Person:
  def __init__(self, name, age): #The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("mohammad", 222)
p1.myfunc()

print("----------------------------------------------")

class Person:
  def __init__(mysillyobject, name, age): #the self parameter can be anything its sumthing just like an name , it can be anything but simpler things are better
    mysillyobject.name = name 
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

p1.age = 40 #you can modify the object properties this way 

p1.myfunc()

del p1.age #and you can delete object properties this way
#or the whole object if you write it without the .age 

print("------------------------------------------")
#casses cant be empty but if you have an empty class to not get an error use the Pass statement

#inheritance in python is used to allow us to define a class that inherits all the methodes and properties from another class

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

class Student(Person): #the new class student will inherit the methodes and properties of the class person
    def __init__(self, fname, lname, year): #the child`s __init__ function will override the parents __init__ function 
       super().__init__(fname, lname) #By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
       self.graduationyear = year
       #person.__init__(self, fname, lname) #To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__()

    def welcome(self):
        print("welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
#  pass #pass its used when you dont want to add anymore methodes or properties to it (also if its empty it will cause an error)

x = Student("Mike", "Olsen" , 2019)
x.welcome()

print("---------------------------------------------------------------------")