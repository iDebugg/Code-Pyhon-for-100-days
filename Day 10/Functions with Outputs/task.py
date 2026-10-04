# def format_name(first_name, last_name):
#     formatted_first_name = first_name.title()
#     formatted_last_name = last_name.title()
#     return f"{formatted_first_name} {formatted_last_name}"
#     print("Hello World")
#
# formatted_string = format_name("john", "doe")
# print(formatted_string)
#



# def function_1(text):
#     return text + " " + text
#
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


is_leap_year(2000)



# def leap_year(year) :
#     if year % 4 == 0 :
#         print(int(input("What is your year")))
#
#
#     return year
