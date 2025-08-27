# day=input("Enter the day of week").lower()

# print(day)

# if day == "saturday" or day =="sunday":
#     print("learn python for devops")
# else:
#     print("learn devops")

num1=int(input("Enter the first num"))
num2=int(input("Enter the second num"))




choice = input("Enter the choice (operator =+ , - . *, /, %)")

if (choice == "+"):
    print("addition", num1+num2)
elif (choice == "-"):
    print("Subtraction" , num1-num2)
elif(choice == "*"):
    print("Multiplication",num1*num2)
elif(choice == "/"):
    print("Division",num1/num2)
else:
    print("Modulus", num1%num2)

