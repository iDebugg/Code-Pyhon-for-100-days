import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]


people_to_pay_bills = random.randint(1, 5)
if people_to_pay_bills == 1 :
    print(friends[0])
elif people_to_pay_bills == 2 :
    print("Bob")
elif people_to_pay_bills == 3 :
    print("Charlie")
elif people_to_pay_bills == 4 :
    print("David")
else :
    print("Emanuel")
