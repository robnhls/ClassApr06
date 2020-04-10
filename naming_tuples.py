from collections import namedtuple


Person = namedtuple("Person", "first_name last_name age city job")


person = Person("alice", "thompson", 39, "buffalo", "engineer")

x = person.first_name
print(x)
