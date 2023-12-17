# Write code that gets three words from a user and inputs them into a sentence using F-Strings
# word_1 = input('Please enter a word \n')
# word_2 = input('Please enter another word \n')
# word_3 = input('Please enter one more word \n')
# print(f'Your words are {word_1}, {word_2} and {word_3}')

# Write a list that contains 2 strings. Print the second string in uppercase and
# then the first string backwards.
# my_list = ['Hello World', 'I love Python']
# first_string = my_list[0]
# reversed_word = ""
# for i in reversed(first_string):
#     reversed_word += i  
# print(reversed_word)
# print(my_list[1].upper())

# Write code for a list that contains four names and prints every other name.
# my_list = ['Elizabeth', 'Aaron', 'Daniel', 'Aria']
# for name in my_list:
#     print(name)

# Write code for a list of numbers. Ask a user for a new number and insert it into the list,
#second from the end.
# numbers_list = [2,45,18,154,369,7,25,57]
# new_num = int(input('Enter any number: \n'))
# numbers_list.insert(-1, new_num)
# print(numbers_list)

# Create a dictionary containing the following information about you: your name,
# your age, your gender, your favorite food. Be sure to use appropriate keys
my_dict = {'my_name':'Elizabeth', 'my_age':'36', 'my_gender':'female', 'my_favirote_food':'sushi'}

# A user is allowed to drive home if their blood alcohol is less than 0.5 %. Ask a
# user for their blood alcohol level and if they're not sober, tell them to take a cab.
# alcohol_level = float(input('What is your blood alcohol level? \n'))
# if alcohol_level > 0.5:
#     print('You are not sober. Take a cab!')
# else:
#     print('Great! Have a good trip!')

# If a user is male and over 65 or female and over 60, they may retire. Get a
# gender and age from the user and let them know if it's time to retire.
gender = input('What is your gender (male/female)? ')
age = int(input('How old are you? '))
if (gender == 'male' and age > 65) or (gender == 'female' and age > 60):
    print('It\'s time to retire')
else: 
    print('It\'s time to work hard')
