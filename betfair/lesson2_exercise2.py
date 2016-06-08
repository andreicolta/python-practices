# Write a Python program to get a string made of the
# first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead
# the empty string.



data = "Write a Python program to get a string made of the " \
       "first 2 and the last 2 chars from a given a string. " \
       "If the string length is less than 2, return instead " \
       "the empty string."

a = {}

for  key in data.split():
    if key.__len__() >= 2:
        print(key[0] + key[1] + key[-2] + key[-1])




#         if word in a:
#             a[word] += 1
#         else:
#             a[word] = 1
#
# #print(a)
#
# for key in a.keys():
#
#         print(key[0] + key[1] + key[-2] + key[-1])


#print(my_list[0:2])
#print(my_list)

# for i in my_list:
#     j = i.replace(' ','')
#     my_list.append(j)
#     print(my_list)