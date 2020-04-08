
ingredients = ["flour", "salt", "water", "sugar", "butter"]


'''
 0 - flour
 1 - salt
 2 - water
 3 - sugar
 4 - butter
'''

# for index in range(0,len(ingredients)):
#     ingredient = ingredients[index]
#     print(f'{index} - {ingredient}')


for index, ingredient in enumerate(ingredients):
    print(f'{index} - {ingredient}')
