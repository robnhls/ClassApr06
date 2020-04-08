

def cool_function(name, fav_food, *fav_movies,
                  print_movies=True, print_attributes=True,
                  **attributes):
    print("Introducing", name)
    print(f"{name} likes {fav_food}")
    if print_movies:
        print("Favorite movies are")
        for movie in fav_movies:
            print("\t", movie)
    if print_attributes:
        print("Other Attributes")
        print(attributes)


cool_function("rob", "tacos", "veggie pizza",
              "steak", "star wars", height="5 foot seven inches", eye_color="green-blue", job="instructor")
