
some_number = 5  # globally





def initialize():
    # global some_number
    some_number = 99


def complicated_function():

    code = 3


    def format(number):
        nonlocal code
        code = 4
        return f"{number:.2f}"


    count = 0  # local
    print("complicated", format(count))
    some_number = 0  # defining a local version of the same name
    print("Complicated", "some_number", format(some_number))




def another_function():

    count = 100  # local
    complicated_function()
    print("another", count)
    print("another", "some_number", some_number)  # global


initialize()
another_function()
print("global", "some_number", some_number)
