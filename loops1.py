total = 0


amount = input("how much did you spend? ")
amount = float(amount)

while amount != 0:
    total = total + amount
    print(f"Current total: {total:.2f}")
    amount = input("how much did you spend? (0 to exit) ")
    amount = float(amount)

print(f"Final total: {total:.2f}")