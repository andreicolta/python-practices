# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?


def ask_number():
    number=int(input("Enter the number: "))
    return number

def check_number(num):
    check=num % 2
    return check

num=ask_number()
result=check_number(num)
if result is 0:
    print("The number is devided by 2")
else:
    print("The number is not devided by 2")

var = True.__doc__



