# Exercise 1 : What Are You Learning?
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

def display_message():
    print('I study Python!!!')
display_message()

# Exercise 2: What’s Your Favorite Book ?
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book(title):
    print(f'One of my favorite books is {title}')

favorite_book('Three man in the boat')

# Exercise 3 : Some Geography
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

def describe_city(city_name, country = 'Spain'):
    print(f"{city_name} is in {country}")

describe_city(city_name = 'Barcelona')

# Exercise 4 : Random
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

import random

def num_random(number):
    num = random.randint(1,100)
    if number == num:
        print('This is success!')
    else:
        print('This is a fail', number, num)

num_random(15)


# Exercise 5 : Let’s Create Some Personalized Shirts !
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

def make_shirt(size, text):
    print(f"The size of the shirt is {size} and the text is {text}")

make_shirt('S', 'Dont worry, be happy!')

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

def make_shirt(size = 'L', text = 'I love Python'):
    print(f"The size of the shirt is {size} and the text is {text}")

make_shirt('L', 'I love Python')
make_shirt('M', 'I love Python')
make_shirt('S', 'Dont worry, be happy!')

# Bonus: Call the function make_shirt() using keyword arguments.

make_shirt(size = 'XS', text = 'Girls rule!')


# Exercise 6 : Magicians …
# Using this list of magician’s names

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Create a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.

def show_magicians(names):
    for name in names:
        print(name)

show_magicians(magician_names)

def make_great(names):
    for name in names:
        print("the Great " + name.title())

make_great(magician_names)


# Exercise 7 : Temperature Advice
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

def get_random_temp():
    return random.randint(-10,40)

temp = get_random_temp()
print(temp)

# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

def main():
    temp = get_random_temp()
    print(f'The temperature right now is {temp} degrees Celsius.')

main()

# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

def main():
    temp = get_random_temp()
    print(f'The temperature right now is {temp} degrees Celsius.')

    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today")
    elif temp >= 0 and temp < 16:
        print("Quite chilly! Don't forget your coat")
    elif temp >= 16 and temp <= 23:
        print("It's mild. Enjoy the pleasant weather!")
    elif temp >= 24 and temp < 32:
        print("Warm day! Stay cool and hydrated!")     
    else: 
        print("Hot weather! Make sure to stay cool!")             

main()

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

def get_random_temp(season):
    if season == 'winter':
        return random.randint(-10,10)
    elif season == 'spring':
        return random.randint(10,20)
    elif season == 'summer':
        return random.randint(25,40)
    else:
        return random.randint(15,25)

temp = get_random_temp('fall')
print(temp)

# Bonus: Give the temperature as a floating-point number instead of an integer.

def get_random_temp(season):
    if season == 'winter':
        return round(random.uniform(-10,10), 1)
    elif season == 'spring':
        return round(random.uniform(10,20), 1)
    elif season == 'summer':
        return round(random.uniform(25,40), 1)
    else:
        return round(random.uniform(15,25), 1)

temp = get_random_temp('fall')
print(temp)

# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

def get_random_temp():
    month = int(input('Enter number of a month: '))
    if month >= 3 and month <= 5:
        return round(random.uniform(10,20), 1)
    elif month >= 6 and month <= 8:
        return round(random.uniform(25,40), 1)
    elif month >= 9 and month <= 11:
        return round(random.uniform(15,25), 1)
    else:
        return round(random.uniform(-10,10), 1)

temp = get_random_temp()
print(temp)


# Exercise 8 : Star Wars Quiz
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.

def quiz():
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []

    random.shuffle(data) 

    for item in data:
        question = item["question"]
        correct_answer = item["answer"]

        user_answer = input(f"\n{question}\nYour answer: ").strip()

        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")
            incorrect_answers += 1
            wrong_answers.append({"question": question, "user_answer": user_answer, "correct_answer": correct_answer})

    return correct_answers, incorrect_answers, wrong_answers

def display_results(correct, incorrect, wrong_answers):
    print("\nQuiz Results:")
    print(f"Correct Answers: {correct}")
    print(f"Incorrect Answers: {incorrect}")

    if incorrect > 0:
        print("\nQuestions you answered incorrectly:")
        for item in wrong_answers:
            print(f"\nQuestion: {item['question']}")
            print(f"Your Answer: {item['user_answer']}")
            print(f"Correct Answer: {item['correct_answer']}")

while True:
    correct_count, incorrect_count, wrong_answers_list = quiz()
    display_results(correct_count, incorrect_count, wrong_answers_list)

    if incorrect_count > 3:
        play_again = input("\nYou had more than 3 wrong answers. Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing. Goodbye!")
            break
    else:
        print("Thanks for playing. Goodbye!")
        break


