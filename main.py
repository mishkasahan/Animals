class Animal:
    def __init__(self, name, species):
        self.species = species
        self.name = name

    def display_info(self):
        print(f"Animal: {self.name} \nSpecies: {self.species}")

class Mammal(Animal):
    def __init__(self, name, species, type_of_food):
        super().__init__(name, species)
        self.type_of_food = type_of_food

    def display_info(self):
        super().display_info()
        print(f"Diet Type: {self.type_of_food}")

class Carnivore(Mammal):
    def __init__(self, name, species, type_of_food, count_teeth):
        super().__init__(name, species, type_of_food)
        self.count_teeth = count_teeth

    def display_info(self):
        super().display_info()
        print(f"Teeth Count: {self.count_teeth}")


class Lion(Carnivore):
    def __init__(self, name, species, type_of_food, count_teeth,  mane_length):
        super().__init__(name, species, type_of_food, count_teeth)
        self.mane_length = mane_length

    def display_info(self):
        super().display_info()
        print(f"Mane Size: {self.mane_length}")




# Створюємо об'єкти різних класів
lion = Lion("Simba", "Lion", "Carnivore", 30, "Large")
carnivore = Carnivore("Tiger", "Carnivore", "Carnivore", 40)
mammal = Mammal("Elephant", "Mammal", "Herbivore")
# Виводимо інформацію про кожну тварину
lion.display_info()
print("-------------------------")
carnivore.display_info()
print("-------------------------")
mammal.display_info()