# Exercise 1 : Convert Lists Into Dictionaries
# Convert the two following lists, into dictionaries.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dic = zip(keys, values)


# Exercise 2 : Cinemax
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# How much does each family member have to pay ?
# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

family = {}
num_family_members = int(input("Enter the number of family members: "))
for i in range(num_family_members):
    name = input(f"Enter the name of family member {i + 1}: ")
    age = int(input(f"Enter the age of {name}: "))
    family[name] = age

total_cost = 0
for age in family.values():
    if age >= 3 and age <= 12:
        total_cost += 10
    elif age > 12:
        total_cost +=15
    else:
        total_cost += 0

print("the family’s total cost for the movie is: ",total_cost)


# Exercise 3: Zara
# Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.
brand = {'name':'Zara', 
        'creation_date':1975,
        'creator_name':'Amancio Ortega Gaona', 
        'type_of_clothes': ['men', 'women', 'children', 'home'],
        'international_competitors': ['Gap', 'H&M', 'Benetton'], 
        'number_stores': 7000, 
        'major_color':{ 
                'France': 'blue', 
                'Spain': 'red', 
                'US': {'pink', 'green'}}
        }

# Change the number of stores to 2.
brand['number_stores'] = 2

# Print a sentence that explains who Zaras clients are.
print("Zara's clients are men, women, and children, and they also offer home products.")

# Add a key called country_creation with a value of Spain.
brand['country_creation'] = 'Spain'

# Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

# Delete the information about the date of creation.
del brand['creation_date']

# Print the last international competitor.
print(brand['international_competitors'][-1])

# Print the major clothes colors in the US.
print(brand['major_color']['US'])

# Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))

# Print the keys of the dictionary.
print(list(brand.keys()))

# Create another dictionary called more_on_zara with the following details:
# creation_date: 1975 
# number_stores: 10 000
more_on_zara = {'creation_date': 1975,
                'number_stores': 10000}

# Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)

# Print the value of the key number_stores. What just happened ?
print(brand['number_stores'])


# Exercise 4 : Disney Characters
#Use this list :
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
#{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
disney_users_A = {}
for i in range(len(users)):
    disney_users_A[users[i]] = i
print(disney_users_A)

# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
disney_users_B = {}
for i in range(len(users)):
    disney_users_B[i] = users[i]
print(disney_users_B)

# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
disney_users_C = {}
sorted_users = sorted(users)
for i in range(len(sorted_users)):
    disney_users_C[sorted_users[i]] = i
print(disney_users_C)

# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
disney_users_with_i = {}
for i in range(len(users)):
    if 'i' in users[i]:
      disney_users_with_i[users[i]] = i       
print(disney_users_with_i)

#The characters, which names start with the letter “m” or “p”.
disney_users_starts_mp = {}
for i in range(len(users)):
    if users[i][0].lower() in ['m', 'p']:
      disney_users_starts_mp[users[i]] = i
        
print(disney_users_starts_mp)



