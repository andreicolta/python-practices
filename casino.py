class Name(object):

    def input_name():
        your_name=input("What is your name: ")
        return your_name



class Greeter(object):

    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello " + self.name)

    def Goodbyy(self):
        print("Goodbye " + self.name)

a=Name
my_name=a.input_name()

g=Greeter(my_name)
g.hello()


