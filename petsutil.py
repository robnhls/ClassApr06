'''
Petsutil

a simple collection of function to read and write is a 
fake pets "database" which is actually a text file

'''

_file_name = "pets.txt"


def read_pets():
    '''
    read_pets()

    reads all of the pets and returns a List
    of the pets

    '''

    list_of_pets = []
    with open(_file_name, "r") as pets_file:
        for p in pets_file:
            list_of_pets.append(p.strip())
    return list_of_pets


def add_pet(pet):
    '''
    add_pet(pet:string)

    add a pet if the pet is not already in the list

    Arguments:
       pet: a string of the pet's name
    '''

    list_of_pets = read_pets()
    if pet not in list_of_pets:
        list_of_pets.append(pet)
        with open(_file_name, "w") as pets_file:
            for p in list_of_pets:
                pets_file.write(p + "\n")


def main():
    # this is code to be run IF we are running directly
    # often it will be test code
    print("we are in main")


if __name__ == "__main__":
    main()
