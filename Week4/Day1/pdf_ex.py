# 1. Write code that gets three words from a user and inputs them into a sentence using F-Strings
# word_1 = input('Please enter a word \n')
# word_2 = input('Please enter another word \n')
# word_3 = input('Please enter one more word \n')
# print(f'Your words are {word_1}, {word_2} and {word_3}')

# 2. Write a list that contains 2 strings. Print the second string in uppercase and
# then the first string backwards.
# my_list = ['Hello World', 'I love Python']
# first_string = my_list[0]
# reversed_word = ""
# for i in reversed(first_string):
#     reversed_word += i  
# print(reversed_word)
# print(my_list[1].upper())

# 3. Write code for a list that contains four names and prints every other name.
# my_list = ['Elizabeth', 'Aaron', 'Daniel', 'Aria']
# for name in my_list:
#     print(name)

# 4. Write code for a list of numbers. Ask a user for a new number and insert it into the list,
#second from the end.
# numbers_list = [2,45,18,154,369,7,25,57]
# new_num = int(input('Enter any number: \n'))
# numbers_list.insert(-1, new_num)
# print(numbers_list)

# 5. Create a dictionary containing the following information about you: your name,
# your age, your gender, your favorite food. Be sure to use appropriate keys
my_dict = {'my_name':'Elizabeth', 'my_age':'36', 'my_gender':'female', 'my_favirote_food':'sushi'}

# 6. A user is allowed to drive home if their blood alcohol is less than 0.5 %. Ask a
# user for their blood alcohol level and if they're not sober, tell them to take a cab.
# alcohol_level = float(input('What is your blood alcohol level? \n'))
# if alcohol_level > 0.5:
#     print('You are not sober. Take a cab!')
# else:
#     print('Great! Have a good trip!')

# 7. If a user is male and over 65 or female and over 60, they may retire. Get a
# gender and age from the user and let them know if it's time to retire.
# gender = input('What is your gender (male/female)? ')
# age = int(input('How old are you? '))
# if (gender == 'male' and age > 65) or (gender == 'female' and age > 60):
#     print('It\'s time to retire')
# else: 
#     print('It\'s time to work hard')

# 8. Write a loop to print every number between 10 and 20.
# for i in range(10,21):
#     print(i)

# 9. Write a loop to print every odd number between 1 and 20.
# for i in range(1, 20):
#     if i%2 != 0:
#         print(i)

# 10. Write code with a list of five names. Print the names one by one using a loop.
# names = ['Ann','Helen','Kerry','Adam','George']
# for name in names:
#     print(name)

# 11. Write a loop that takes numbers from the user until it receives the number 0
# and prints the sum of the numbers received.
# sum = 0
# while True:
#     num = int(input('Enter a number '))
#     if num == 0:
#         break
#     else:
#         sum += num
# print(sum)

# 12. Exercise: Write a loop that takes words from the user until it receives the word 'done' and
# prints the longest word received.
# longest_word = ''
# while True:
#     word = input('Enter a word: ')
#     if word == 'done':
#         break
#     else:
#         if len(word) > len(longest_word):
#             longest_word = word      
# print(longest_word)


# 13. Write a function that takes a string as input and prints its length:
def length(string):
    return len(string)

input_string = 'I love Python'
print(length(input_string)) 

# 14. Exercise: Define a function that takes three numbers and prints their average.
def avg_numbers(number1, number2, number3):
    return print((number1+number2+number3)/3)

avg_numbers(25, 12, 4)

# 15. Exercise: Define a function that takes two arguments, a string and a number and checks
# if the string has more characters than the number. Example: 'string', 3 prints True since
# string has 5 characters.
def what_longer(string, number):
    return len(string) > number

input_string = 'I love Python'
input_number = 5

result = what_longer(input_string, input_number)
print(result)

# 16. Exercise: Write a function that copies a string a certain number of times, based on the
# input. Set the default amount of copies to be 1.
def copy_string(input_string, num_copies=1):
    return input_string * num_copies

original_string = 'Hello, world! '
num_copies = int(input('Enter any number: '))
result = copy_string(original_string, num_copies)
print(result)

original_string = 'Hello, world! '
num_copies = int(input('Enter any number: '))
result = copy_string(original_string, num_copies)
print(result)

