# Write a program to input two messages and output them to a user.
# Write a program to input two whole numbers, add them together and print the result to the screen.
# Tip: When inputting numbers, use int(input()) instead of input() - more on this later.


msg1 = input("Enter the first word: ")
msg2 = input("Enter the second word: ")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("First word is:" + msg1 + " and second word is: " + msg2 )


numbers = num1 + num2
print("Sum of numbers is: {} ".format(numbers))