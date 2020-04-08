file_name = r"C:\class\pets.py"

with open(file_name, "r") as pets_file:

    # for pet in pets_file:
    #     pet = pet.strip()  #get rid of the newline at the end of each line
    #     print(f"hello {pet}")

    # load file into memory
    pets = [pet.strip() for pet in pets_file]

print("We have all the pets")

print("Enter a new pet")
new_pet = input("New pet name")
pets.append(new_pet)
# validataion

# the with block closes the pets_file automatically
with open(file_name, "w") as pets_file:
    for p in pets:
        pets_file.write(p + "\n")  # add the newline


print("File updated")
