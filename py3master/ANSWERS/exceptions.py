
numbers = [1, 2, 3, 4, 5, 6, 7, "8", 9, 10, 11, -10]

# ZeroDivisionError
# TypeError
data = []

base_number = 10
for n in numbers:

    try:
        step1 = n + base_number
        step2 = 100 / step1
        print("The result of adding", n, "and", base_number, "is", step1)
        print("The final result is ", step2)
    except ZeroDivisionError:
        print("The answer is 0")
    except TypeError:
        print(f"Input is wrong. Value '{n}' is not a number")
    except Exception as err:
        print(f"unknown error with value {n}")
        print(f"Error information: {err}")
    else:
        data.append(n)
    finally:
        print("-" * 20)


print("Processed Data", data)

