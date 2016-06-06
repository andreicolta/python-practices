# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they
# will turn 100 years old.


import datetime

time_now=datetime.datetime.now()
your_name=input("Enter your Name: ")
your_age=int(input("What is your age: "))
year=time_now.year

the_year=((100-your_age)+year)

print("The year when you will have 100 will be + %s" %(the_year))





