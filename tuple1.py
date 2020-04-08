person = ("rob", "instructor", "detroit", 47)

person2 = "Gayle", "Contractor", "columbus", 61

person3 = "beth", "sales", "san diego", 57

person4 = "jack", "programmer", "woodlands", 50

numbers = 3, 4

so_many_people = [person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  person, person2, person3, person4,
                  ("Janelle", "programmer", "Columbus", 29)]


# this is an example of unpacking
# underscore is used as a variable because we do not need it,
# but we are forced to define it


# names = []
# for name, job, city, age in so_many_people:
#     if job == "programmer":
#         names.append(name)

names = [name
         for name, job, _, _ in so_many_people
         if job == "programmer"]

count = 1
for n in names:
    print(n)
    count = count + 1
    if count > 3:
        break
