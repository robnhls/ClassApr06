dinner = input("What are we having for dinner?")

time = "6:00"

attending = input("How many will be attending?")
size = input("Portion size in oz")

attending = int(attending)  # convert attending to an integer
size = int(size)          # convert size to a fload (decimal)

menu = f"{dinner} will be served at {time}"
food_prepared = attending * size

print(menu)
print(f"we will prepare {food_prepared} oz of dinner")
