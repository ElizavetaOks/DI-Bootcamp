# Exercise 1: Cats
# Using this class

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

first_cat = Cat('Angel', 5)
second_cat = Cat('Lily', 2)
third_cat = Cat('Bella', 7)

def find_oldest_cat(cat):
    if first_cat.age > second_cat.age and first_cat.age > third_cat.age:
        oldest_cat = first_cat
    elif second_cat.age > first_cat.age and second_cat.age > third_cat.age:
        oldest_cat = second_cat
    else:
        oldest_cat = third_cat

    return oldest_cat

oldest_cat = find_oldest_cat([first_cat,second_cat,third_cat])

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

print('-'*20)


# Exercise 2 : Dogs
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height
        
    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        x = self.height*2
        print(f'{self.name} jumps {x} cm high!')

davids_dog = Dog('Rex', 50)

print(davids_dog.name, davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', 20)

print(sarahs_dog.name, sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
    print(f"The bigger dog is {sarahs_dog.name}.")
else:
    print("Both dogs are of the same height.")

print('-'*20)


# Exercise 3 : Who’s The Song Producer?
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:

class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics

def sing_me_a_song(self):
    for i in self.lyrics:
        print(i)

stairway= Song(["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"])

sing_me_a_song(stairway)

print('-'*20)


# Exercise 4 : Afternoon At The Zoo
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).

class Zoo():
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
    def add_animal(self, new_animal):
            if new_animal not in self.animals:
                self.animals.append(new_animal)
            else:
                print('The animal is in the list')

# Create a method called get_animals that prints all the animals of the zoo.
    def get_animals(self):
        print(self.animals)

# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        groups = {}
        for animal in sorted_animals:
            first_letter = animal[0]
            if first_letter not in groups:
                groups.update({first_letter:[animal]})
            else:
                groups[first_letter].append(animal)

        return groups

# Create a method called get_groups that prints the animal/animals inside each group.
    def get_groups(self):
        group_dict = self.sort_animals()
        new_dict = {}
        for i, group in enumerate(group_dict):
            new_dict.update({i+1: group_dict[group]})

        return new_dict

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.

ramat_gan_safari = Zoo("Ramat Gan Safari")

ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Llama")

ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Giraffe")

ramat_gan_safari.get_animals()

print(ramat_gan_safari.sort_animals())

print(ramat_gan_safari.get_groups())
