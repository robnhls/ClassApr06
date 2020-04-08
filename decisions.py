

people = input("How many people? ")  # str
people = int(people)

size = input("What size portion (s, m, l) ")

if size == "s":
    oz = 6.0
    print(f"We will prepare a small portion of {oz} oz.")
elif size == "m":
    oz = 8.0
    print(f"We will have a medium portion ready for you")
else:
    oz = 12.0
    print("Large portions coming up.")


amount = people * oz

# when we really don't need an entire if block
# contitional assignment
label = "person" if people == 1 else "people"

# if people == 1:
#     label = "person"
# else:
#     label = "people"

print(f'We will prepare {amount} oz of food for {people} {label}.')
