
list_animals = []

for i in range(6):
    i = str(input("Enter the animal name: "))

    list_animals.append(i)


ask_user = str(input("Print List in reverse order Yes/No: "))

if ask_user == "Yes":
    list_animals.reverse()

print(list_animals)


ask_number = int(input("Enter a number from 1 to 6: "))

print(list_animals[ask_number -1])





