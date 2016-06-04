a = int(input("Numbers: "))

average = 0
suma = 0

for i in range(a):
    suma = suma + int(input("Enter number %d :" %(i)))

average = suma / a

print("Average of " + a + ":" + " is" + average)

