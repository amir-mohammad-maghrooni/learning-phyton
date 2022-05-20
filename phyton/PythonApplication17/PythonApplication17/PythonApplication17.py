
import datetime
t = datetime.datetime.now()

print(t)
print("hello and welcome to X company")

username = input("please enter your username: ")
print("welcome back", username)

print("it has been a long time since your last login \nwe must ask you to re enter you`r profile detail`s")

I = "no"

while I == "no" :
    Fname = input ("please enter you`r First name: ")
    Lname = input ("please enter you`r Last name: ")
    Age = input ("please enter you`r Age: ")
    Gender = input("please enter your Gender: ")

    question = input("would you like to enter your address ? (y/n)")
    
    if question == "y":
        Address = input ("please enter you`r address: ");
    else:
        Address = "NA";
    
    question = input ("would you like to enter your email ? (y/n)")
    if question == "y":
        Email = input = ("please enter you`r Emaail Address: ")
    else:
        Email = "NA"

    print(Fname ,"\n" ,Lname ,"\n" ,Age ,"\n" ,Gender ,"\n" ,Address ,"\n",)
   
    I = input ("are these correct?(yes/no): ")

print(username + " You have some uncompleted purchese`s!")
I = "no"
while I == "no":
    
    print ("you`r last purchase of groceries and home goods have not yet been send to you!")

    question = input ("would you like to change your address?\n(if no address is in the profile you are forced to enter your address)(y/n): ")
    if Address == "NA" & question == "y":
        Address = input ("please enter your address: ")

    print ("your purchase will be sent to the address\n" ,Address)

    I = input ("Is this address correct?(yes/no")


print("thank you for using the X company`s service`s")