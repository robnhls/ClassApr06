
names = ["MichaelB", "MichaelL", "Paul", "Rolondo", "Todd"]
# towns = ["Columbus", "Miami", "St. Paul", "NYC", "Bowie"]

towns = {"Rolondo": "NYC", "MichaelB": "Columbus", "MichaelL": "Miami",
         "Paul": "St. Paul", "Todd": "Bowie"}


location = towns["Paul"]

print(location)

# BTW - Pandas is a great lib for data


results = {}

with open("votes.txt", "r") as votes:
    for vote in votes:
        name = vote.strip().lower()
        if name in results:
            results[name] += 1
        else:
            results[name] = 1

# print(results)
for name, votes in results.items():
    print(f"{name} received {votes} votes(s)")

# just the keys
for name in results:
    print(name)

# the number of votes that rob got
if "rob" not in results:
    print("Rob got 0 votes")
else:
    print(f"rob got {results['rob']} votes")

# option # 2
print(f"rob got {results.get('rob', 0)} votes")
