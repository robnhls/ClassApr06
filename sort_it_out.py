names = ["Clayton", "Jimmy", "Gayle", "Jack", "Janelle", "Jason"]
numbers = [12, 45, 98, 2, 54, 1004, 50, 12]
pets = [
    "Larry",
    "Tabu",
    "Jeff",
    "togo",
    "sunset",
    "snoopy",
    "yoyo",
    "suki",
    "cindy",
    "Kujo the cybernetically enhanced spider monkey",
    "dutchess",
    "buttons",
    "Shadow",
]

person = ("rob", "instructor", "detroit", 47)
person2 = "Gayle", "Contractor", "columbus", 61
person3 = "beth", "sales", "san diego", 57
person4 = "jack", "programmer", "woodlands", 50
person5 = "jack", "contractor", "woodlands", 50


so_many_people = [person, person2, person3, person4, person5,
                  ("Janelle", "programmer", "Columbus", 29)]


def fix_strings(s):
    return s.lower().strip()


def by_length(pet):
    return len(pet)


# def awesome_sort(pet):
#     return (len(pet), fix_strings(pet))


sorted_pets = sorted(pets, key=lambda pet: (len(pet), fix_strings(pet)))


# for p in sorted_pets:
#     print(p)


def name_then_city(person):
    return (person[0].lower(), person[2].lower())


sorted_people = sorted(so_many_people, key=name_then_city)

for p in sorted_people:
    print(p)
