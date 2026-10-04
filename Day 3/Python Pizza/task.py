size = input("What pizza size do you want ? ")
pepperoni = input("Do you want pepperoni? Y OR N ")
cheese = input("Do you want cheese? Y OR N ")
if size == "S" :
    Bill = 15
    if pepperoni == "Y" :
        Bill += 2
        if cheese == "Y" :
            Bill += 1
            print("Your bill is $" + str(Bill))
        elif cheese == "N":
            print("Your bill is $" + str(Bill))
        else:
            print("wrong  input")
    elif pepperoni == "N" :
        print("Your bill is $" + str(Bill))
    else:
        print("wrong  input")
elif size == "M" :
    Bill = 20
    print("Your bill is $" + str(Bill))

elif size == "L" :
    Bill = 25
    print("Your bill is $" + str(Bill))

else :
    print("wrong size input")