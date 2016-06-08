from random import randint

my_list = []
freqs = {}

def randome_number():
    number_rand = randint(1,6)
    return number_rand

for i in range(30):
    a  = randome_number()
    my_list.append(a)

for num in my_list:
    if num in freqs.keys():
        freqs[num] += 1
    else:
        freqs[num] = 1


# print(my_list)
print(freqs)
