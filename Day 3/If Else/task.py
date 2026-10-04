print("welcome back Victor")
height = int(input("enter your height: "))
# print(height)
if height == 120:
    age = int(input("enter your age: "))
    if age < 12 :
        print("your money is $5")
    elif age <18:
        print("your money is $7")
    else :
        print("your money is $12")

else:
    print("cant ride")
