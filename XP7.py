# Exercise 1 : Pets
# Using this code:

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bengal_cat = Bengal(name="BengalCat", age=3)
chartreux_cat = Chartreux(name="ChartreuxCat", age=4)
siamese_cat = Siamese(name="SiameseCat", age=2)
    
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

sara_pets = Pets(all_cats)

sara_pets.walk()

print('_'*20)


# Exercise 2 : Dogs
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f'{self.name} won the fight!'
        elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
            return f'{other_dog.name} won the fight!'
        else:
            return 'It was a draw!'

dog1 = Dog(name="Rex", age=3, weight=15)
dog2 = Dog(name="Max", age=4, weight=20)
dog3 = Dog(name="Buddy", age=2, weight=18)

print(dog1.bark())

print(f'{dog2.name}\'s running speed is {dog2.run_speed()}')

print(dog1.fight(dog2))

print('_'*20)


# Exercise 3 : Dogs Domesticated
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
    # Add the following methods:
    # train: prints the output of bark and switches the trained boolean to True
    # play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.
    # do_a_trick: If the dog is trained the method should print one of the following sentences at random:
        # “dog_name does a barrel roll”.
        # “dog_name stands on his back legs”.
        # “dog_name shakes your hand”.
        # “dog_name plays dead”.

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f'{self.name} won the fight!'
        elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
            return f'{other_dog.name} won the fight!'
        else:
            return 'It was a draw!'
        
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        bark_output = super().bark()
        print(bark_output)
        self.trained = True

    def play(self, *dog_names):
        print(f'{", ".join(dog_names)} all play together')

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f'{self.name} does a barrel roll',
                f'{self.name} stands on his back legs',
                f'{self.name} shakes your hand',
                f'{self.name} plays dead'
            ]
            selected_trick = random.choice(tricks)
            print(selected_trick)
        else:
            print(f'{self.name} is not trained. Train the dog to see tricks!')

pet_dog = PetDog(name="Milly", age=3, weight=15)

pet_dog.train()

pet_dog.play("Max", "Charlie")

pet_dog.do_a_trick()

print('_'*20)


# Exercise 4 : Family
# Create a class called Family and implement the following attributes:

# members: list of dictionaries
# last_name : (string)

# Implement the following methods:
# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ details.

# Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.

#     [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False}
#     ]

class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **child):
        self.members.append(child)
        print(f"Congratulations! {child['name']} is born in the {self.last_name} family.")

    def is_18(self, family_member_name):
        for member in self.members:
            if member['name'] == family_member_name:
                return member['age'] >= 18
        return False 

    def family_presentation(self):
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Child: {member['is_child']}")

family_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

family_instance = Family(last_name="Dou", members=family_members)

family_instance.born(name='John', age=0, gender='Male', is_child=True)

print(f"Is Michael over 18? {family_instance.is_18('Michael')}")

family_instance.family_presentation()

print('_'*20)


# Exercise 5 : TheIncredibles Family
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore the members attributes, will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)

# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.

# Add a method called incredible_presentation which :

# Print a sentence like “*Here is our powerful family **”
# Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)

# Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members.
#     [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
#     ]

# Call the incredible_presentation method.
# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# Call the incredible_presentation method again.

class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, member_name):
        for member in self.members:
            if member['name'] == member_name:
                if member['age'] >= 18:
                    print(f"{member['incredible_name']} uses the power: {member['power']}")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old and cannot use their power.")

    def incredible_presentation(self):
        print("*Here is our powerful family*")
        super().family_presentation()

incredibles_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

incredibles_instance = TheIncredibles(last_name="Incredibles", members=incredibles_members)

incredibles_instance.incredible_presentation()

incredibles_instance.born(name='Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='BabyJack')

incredibles_instance.incredible_presentation()


