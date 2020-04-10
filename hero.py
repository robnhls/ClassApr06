
class Hero:
    # constructor / initializer
    def __init__(self, name, superpower):
        self._name = name
        self._superpower = superpower
        self._worlds_saved = 2

    @property
    def name(self):
        return self._name

    @property
    def superpower(self):
        return self._superpower

    @property
    def worlds_saved(self):
        return self._worlds_saved

    @worlds_saved.setter
    def worlds_saved(self, number_of_saved_worlds):
        # words saved can only increase
        if self._worlds_saved <= number_of_saved_worlds:
            self._worlds_saved = number_of_saved_worlds
        else:
            raise ValueError("worlds_saved can only increase")

    def introduce(self):
        return f"The name is {self._name}. I have saved the world {self._worlds_saved} times."

    def save_the_world(self):
        return f"{self._name} saves the world with {self._superpower}."


# ---- somewhere else
h1 = Hero("Cool Hero", "Super Speed")
h2 = Hero("rob.in.hood", "only hiccups 3 times")

h1.worlds_saved = -2

message = h1.save_the_world()
print(message)

message = h1.introduce()
print(message)
