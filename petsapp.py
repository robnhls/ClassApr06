
from petsutil import read_pets, add_pet

print("Current Pets")
pets = read_pets()  # read_pets is a function in the petsutil.py file

for p in pets:
    print(p)


pet_name = input("Add a new pet: ")
if pet_name:
    add_pet(pet_name)


print("Current Pets")
pets = read_pets()  # read_pets is a function in the petsutil.py file


