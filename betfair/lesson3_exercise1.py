# Write a program that will ask the user for a message and
# the number of times they want that message displayed.
# Then output the message that number of times.
# Write a program that will calculate the average (mean)
# of a set of numbers. This time, the user is to be asked
# how many numbers are to be averaged, they must then enter
# this number of numbers. Your program will calculate and
# display the average of those numbers.

a = int(input("Numbers: "))

average = 0
suma = 0

for i in range(a):
    suma = suma + int(input("Enter number %d :" %(i)))

average = suma / a

print("Average of " + a + ":" + " is" + average)

