try :
    age = int(input("How old are you?"))
except :
    print("You have typed in a a wrong value, pls type in numerical value")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
