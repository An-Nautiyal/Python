#PROGRAMER INTRODUCTION
print("Hello World!")
print("My name is Anshul Nautiyal. \nI am mastering python here please support me in my journey!")
#STARTING THE BASIC PROGRAMMING
print("Starting basic python programming!")
#Write a program to display a person's name, age and address.
name = input("Enter your Name : ")
age = int(input ("Enter your age : "))
adrs =  input("Enter your City : ")
print(f"Name : {name}\nAge : {age}\nAddress : {adrs}")
#write a program to swap twp variables.
fvar =int(input("Enter first no: "))
svar =int(input("Enter second no: "))
print(f"First No. is {fvar}\nSecond No. is {svar}\nAfter swaping-")
#After Swaping
fvar,svar = svar,fvar
print(f"First No. : {fvar}\nSecond No. : {svar}")
#write a program to convert a float into integer.
no =float(input("Enter  a Float no : "))
nu = int(no)
print("After conversion new no is : ",nu)
#write a program to take details from student for ID card.
NAME =input("Enter your Name : ")
AGE =int(input ("Enter your age : "))
CITY =input("Enter your City : ")
ROLL =int(input("Enter your Roll.No : "))
CLASS =input("Enter your class : ")
print(f"==-==-=ID CARD=-==-==\n{NAME}\n{age}\n{CITY}\n{ROLL}\n{CLASS}\n==-==-==-==-==")
