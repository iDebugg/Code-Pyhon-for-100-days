def add(n1, n2):
    return n1 + n2

def sub(n1, n2) :
    return n1 - n2

def div(n1, n2) :
    return n1 / n2

def mul(n1, n2) :
    return n1 * n2


operations = {
    "+" : add ,
    "-" : sub,
    "/" : div,
    "*" : mul,
}
def calculator () :
    first_number = float(input("Type your first number "))
    for symbol in operations :
        print(symbol)
    should_continue = True
    while should_continue :
        operator_type = input("Type your operator: ")
        second_number = float(input("Type your second number "))

        my_favorite_task = operations[operator_type]
        answer = my_favorite_task(first_number, second_number)
        print(answer)
        to_use_first_result = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation ")
        if to_use_first_result == "y" :
            first_number = answer
        else :
            should_continue = False
            calculator()

calculator()

