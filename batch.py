import sys

# expected execution
# python batch.py chicken 5 6.5
# there is a small problem
dinner = sys.argv[1]
attending = sys.argv[2]
size = sys.argv[3]

time = "6:00"

attending = int(attending)  # convert attending to an integer
size = float(size)          # convert size to a fload (decimal)

menu = f"{dinner} will be served at {time}"
food_prepared = attending * size

print(menu)
print(f"we will prepare {food_prepared} oz of dinner")
