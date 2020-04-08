total = 0


while True:
    amount = input("how much did you spend? (0 to exit) ")
    amount = float(amount)
    total = total + amount
    print(f"Current total: {total:.2f}")

    if amount == 0:
        break # exit the loop

print(f"Final total: {total:.2f}")