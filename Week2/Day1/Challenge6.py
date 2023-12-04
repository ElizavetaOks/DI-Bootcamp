# Old MacDonald’s Farm

# Create a class called Farm. How should it be implemented?
# Does the Farm class need an __init__ method? If so, what parameters should it take?
class Farm():
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, quantity=1):
        animal_type = animal_type.lower()
        if animal_type in self.animals:
            self.animals[animal_type] += quantity
        else:
            self.animals[animal_type] = quantity

    def get_info(self):
        info = f"{self.name}'s farm\n"
        for animal, quantity in self.animals.items():
            info += f"{animal} : {quantity}\n"
        info += "E-I-E-I-0!"
        return info

# Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal types (names) in the farm. 
# With the example above, the list should be: ['cow', 'goat', 'sheep'].
    
    def get_animal_types(self):
        return sorted(list(self.animals.keys()))

# Add another method to the Farm class called get_short_info. This method should return the following string: “McDonald’s farm has cows, goats and sheep.”. 
# The method should call the get_animal_types function to get a list of the animals.   

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_str = ", ".join(animal_types)
        return f"{self.name}'s farm has {animal_str}."
    
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
