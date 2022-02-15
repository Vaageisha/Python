#Basic calculator-for solvingairthemetic operation on integer values.
name = input("Enter your name: ")   
user_name= name                          #to ask for user input
print("Hello", user_name ,"Welcome to the computer application") 

num1=int(input("Enter first integer number"))                        #asking user for numbers to perform operation on
num2= int(input("Enter second integer number"))

choice= int(input ('''for addition input value 1,
for subraction input value 2
for multiplication input value 3
for division input value 4
for modulus input value 5''') )                             #asking user to choose for an airthemetic operation


if(choice==1):
    print("The addition of",num1,"and",num2, num1+num2)
exit

if(choice==2):
       print("the subtraction of",num1, "and",num2, num1-num2)
exit

if(choice==3):
    print("the product for", num1, "and", num2, num1*num2)
exit

if(choice==4):
    print("the remainder for", num1, "and", num2, num1/num2)
exit

if(choice==5):
    print("the modulus for", num1, "and", num2, num1%num2 )
exit

print("thankyou for using the calculator program!")



    
    









