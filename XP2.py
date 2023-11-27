# Exercise 1 : Set
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {3,5,7}
my_fav_numbers.add(15)
my_fav_numbers.add(77)
my_fav_numbers.remove(77)
friend_fav_numbers = {3,13,30,10}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)


# Exercise 2: Tuple
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# A tuple is an in immutable type, we cannot add or remove elements in a tuple.


# Exercise 3: List
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Banana')
basket.remove('Blueberries')
basket.append('Kiwi')
basket.insert(0,'Apples')
apple_count = basket.count('Apples')
print(f'{apple_count} apples are in the basket')
basket.clear()
print(basket)


# Exercise 4: Floats
# Recap – What is a float? What is the difference between an integer and a float?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?

my_list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
my_list2 = [i/2 for i in range(3, 11)]
print(my_list)
print(my_list2)


# Exercise 5: For Loop
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

for num in range(1, 21):
    print(num, end=' ')

for num in range(1, 21):
    if num % 2 == 0:
        print(num, end=' ')


# Exercise 6 : While Loop
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

your_name = ''
while your_name != 'Elizaveta':
    your_name = input('What is your name? ')
print('You have beautiful name!')

# Exercise 7: Favorite Fruits
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

fav_fruits = input("Enter your favorite fruit(s) separated by a single space: ")
favorite_fruits = fav_fruits.split()
fruit = input("Enter a name of a fruit: ")
if fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy.")


# Exercise 8: Who Ordered A Pizza ?
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

toppings = []
total_price = 10
while True:
    topping = input("Enter a pizza topping (type 'quit' to finish): ")
    if topping == 'quit':
        break
    toppings.append(topping)
    total_price += 2.5
    print("We'll add that topping to your pizza.")
for topping in toppings:
    print("Toppings: ", topping)
print("Total Price: ", total_price)


# Exercise 9: Cinemax
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

family_ages = []
num_people = int(input("Enter the number of people in your family: "))
total_cost = 0
for i in range(num_people):
    age = int(input(f"Enter the age of person {i + 1}: "))
    family_ages.append(age)
    if age < 3:
        total_cost += 0
    elif 3 <= age <= 12:
        total_cost += 10
    else:
        total_cost += 15
print(f"Total cost of tickets for the family: {total_cost}$")

teenagers = ["David", "Ron", "Aria", "Liza", "Eva"]
allowed_teenagers = []
for teenager in teenagers:
    age = int(input(f"Enter the age of {teenager}: "))
    if 16 <= age <= 21:
        allowed_teenagers.append(teenager)
print(allowed_teenagers)


# Exercise 10 : Sandwich Orders
# Using the list below :
# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich}")