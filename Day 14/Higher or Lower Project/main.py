import random
from art import logo, vs
from game_data import data


print(logo)
print("Compare A: ...")
print(vs)
print("Against B: ...")

score = 0
game_should_continue =  True
random_account_b = random.choice(data)

def format_data (account) :
    account_name  = account["name"]
    account_decr = account["description"]
    account_country = account["country"]
    account_follower = account["follower_count"]
    return (f"{account_name} a {account_decr} from {account_country} {account_follower} ")

while game_should_continue :
    random_account_a = random_account_b
    random_account_b = random.choice(data)

    if random_account_a == random_account_b :
        random_account_b = random.choice(data)



    print(f"Compare A : {format_data(random_account_a)}")
    print(vs)
    print(f"Against B : {format_data(random_account_b)}")

    human_Guess = input("Who has more followers? Type 'A' or 'B' : ")
    a_follower_count = random_account_a["follower_count"]
    b_follower_count = random_account_b["follower_count"]

    if human_Guess == "A" and a_follower_count > b_follower_count :
        score += 1
        print(f"You are right ! Current score : {score}")

    elif human_Guess == "A" and a_follower_count < b_follower_count :
        score = score
        print(f"Sorry thats wrong, final score : {score}")
        game_should_continue = False


    elif human_Guess == "B" and a_follower_count < b_follower_count :
        score += 1
        print(f"You are right ! Current score : {score}")

    elif human_Guess == "B" and a_follower_count > b_follower_count :
        score = score
        print(f"Sorry thats wrong, final score : {score}")
        game_should_continue = False




