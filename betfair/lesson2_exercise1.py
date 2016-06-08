#Write a Python program to calculate the length of a string
import collections

data = "Write a Python program to calculate the length of a string"

# print(len(data))
#
# List = list(data)
# print(List)
#
# Uniq = set(data)
# print(Uniq)

#Write a Python program to count the number of characters (character frequency) in a string.

freqs = {}

for line in data:
    for char in line:
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1
print(freqs)


# for i in data:
#     count = 0
#     count = data.count(i)
#     if count > 1:
#         print(i, count)



