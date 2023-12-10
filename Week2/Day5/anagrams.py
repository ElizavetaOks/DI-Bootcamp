# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.

# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.

# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:

from anagram_checker import AnagramChecker 

if __name__ == "__main__":
    word_list_file = 'sowpods.txt'
    anagram_checker = AnagramChecker(word_list_file)

    while True:
        print("\nMenu:")
        print("1. Input a word")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            user_word = input("Enter a word: ").strip()
            
            if ' ' in user_word:
                print("Error: Only a single word is allowed.")
                continue

            if not user_word.isalpha():
                print("Error: Only alphabetic characters are allowed.")
                continue

            user_word = user_word.strip()

            if anagram_checker.is_valid_word(user_word):
                anagrams = anagram_checker.get_anagrams(user_word)

                print(f'\nYOUR WORD: "{user_word.upper()}"')
                print("This is a valid English word.")
                print("Anagrams for your word:", ', '.join(anagrams) if anagrams else "None.")
            else:
                print(f'\nYOUR WORD: "{user_word.upper()}"')
                print("This is not a valid English word.")
        elif choice == '2':
            print("Exit program. Goodbye!")
            break
        else:
            print("Wrong choice. Please enter 1 or 2.")