

def input_number():
    miki = int(input("Enter number:"))
    return miki


def data_valid(num):

    if num % 7 == 0:
        return True
    return False


result=input_number()

print(result)
def outputData(result):
    if result is True:
        print("Number is divisible with 7")

    else:
        print("This number is not divisible with 7")


data=data_valid(result)

outputData(data)





