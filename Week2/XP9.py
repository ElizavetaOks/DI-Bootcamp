# Exercise 1 – Random Sentence Generator
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

import random
import string

def get_words_from_file(file_name):
    try:
        with open('sowpods.txt', 'r') as f:
            words = f.read().split()
        return words
    except FileNotFoundError:
        print("Error: File not found.")
        return []

def get_random_sentence(words, length):
    if length < 2 or length > 20:
        print("Error: Sentence length should be between 2 and 20.")
        return None

    random_words = random.sample(words, length)
    sentence = ' '.join(random_words)
    return sentence.lower()

def main():
    print("Welcome to the Random Sentence Generator!")

    words = get_words_from_file('sowpods.txt')

    if not words:
        print("Exiting program.")
        return

    try:
        sentence_length = int(input("How long do you want the sentence to be (between 2 and 20)? "))
        if 2 <= sentence_length <= 20:
            sentence = get_random_sentence(words, sentence_length)
            if sentence:
                print("Random Sentence:", sentence)
        else:
            print("Error: Invalid sentence length. Exiting program.")
    except ValueError:
        print("Error: Please enter a valid integer. Exiting program.")

if __name__ == "__main__":
    main()



#Exercise 2: Working With JSON

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


# Access the nested “salary” key from the JSON-string above.
data = json.loads(sampleJson)

salary_value = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary_value)

# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
data["company"]["employee"]["birth_date"] = "1990-01-01"

# Save the dictionary as JSON to a file.

output_file_path = "output.json"
with open(output_file_path, "w") as output_file:
    json.dump(data, output_file, indent=2)

print(f"Modified JSON saved to {output_file_path}")