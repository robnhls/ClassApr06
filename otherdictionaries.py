
from collections import defaultdict


def default_gift_maker():
    return "a rock"


gifts = defaultdict(lambda: "a rock")
gifts["janelle"] = "car"
gifts["gayle"] = "flowers"
gifts["michael"] = "scientific model"

print(gifts["rob"])
