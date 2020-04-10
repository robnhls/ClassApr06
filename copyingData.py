import copy
from pprint import pprint
from collections import defaultdict


firstList = ["money", "vaccine", "gift card", "puppy"]

firstList.append(["Jewelry", "diamonds", "gold"])
secondList = copy.deepcopy(firstList)
thirdList = list(firstList)

secondList[4].append("yatch")

secondList.append("hand sanitizer")
thirdList.append("Clothing")

gifts = defaultdict(lambda: "a rock")
gifts["janelle"] = "car"
gifts["gayle"] = "flowers"
gifts["michael"] = "scientific model"

greedy = [firstList, gifts, secondList, thirdList]


# debugging / troubleshooting
print(greedy)
print("----------------------------")
pprint(greedy)
