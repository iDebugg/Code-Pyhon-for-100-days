print("welcome back Victor")
height = int(input("enter your height: "))
# print(height)
Bill = 0
if height == 120:
    age = int(input("enter your age: "))
    if age < 12 :
        Bill = 5
        print("ypur bill is " + str(Bill))
    elif age <18:
        Bill = 7
        print("ypur bill is " + str(Bill))
    else :
        Bill = 12
        print("ypur bill is " + str(Bill))

    wants_photo = input("Do you want photos, type y for Yes and n for No: ")
    if wants_photo == "y":
        total_bills = Bill + 3
        print("Your total bill is " + str(total_bills))
    elif wants_photo == "n":
        total_bills = Bill
        print("Your total bill is " + str(total_bills))
    else:
        print("please enter y or n")

else:
    print("cant ride")
