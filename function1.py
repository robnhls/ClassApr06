import sys
# expected usage
# python <fileName> number_of_iterations:int

results = {}


def initialize_data():
    with open("votes.txt", "r") as votes:
        for vote in votes:
            name = vote.strip().lower()
            if name in results:
                results[name] += 1
            else:
                results[name] = 1


def get_votes(person):
    person = person.lower()
    if person not in results:
        return 0
    else:
        return results[person]


def print_help():
    print("The Cool Application")
    print("To use the script you will need to pass in the number of iterations")
    print("ex ...")
    print("python <fileName> 5")


def actual_work(number_of_iterations):
    for count in range(number_of_iterations):
        print("doing work")


# coordination
if len(sys.argv) < 2:
    print_help()
else:
    initialize_data()

    robs_votes = get_votes("ROB")
    claytons_votes = get_votes("Clayton")
    gayles_votes = get_votes("gayle")

    print("rob", robs_votes)
    print("clayton", claytons_votes)
    print("gayle", gayles_votes)
