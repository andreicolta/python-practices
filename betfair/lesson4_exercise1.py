# EXERCISE #2
# inputData() - this function will input a number from the user and return it.
# processData(number) - this function will see if the number is divisible by 7
# without a remainder and if it is it will return True otherwise false.
# Tip - use the integer division // and the remainder % operators for this.
# outputData(result) - this function will input the value from the previous
# function and print a user friendly message at the screen.
# main() - this function will call the three functions above to run the whole program


def input_str():
    my_string= input("Enter the string:")

    return my_string

def string_len(my_string):
    str_len= len (my_string)

    return str_len

def reverse_string(input_str):
    reversed=""
    for a in range(string_len(input_str) -1,-1,-1) :
        print(a)
        reversed += input_str[a]

    return reversed


in_txt= input_str()
# print()
print(reverse_string(in_txt))
