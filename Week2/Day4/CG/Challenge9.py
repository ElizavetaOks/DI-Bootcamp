
# Daily Challenge : Text Analysis

# The goal of the exercise is to create a class that will help you analyze a specific text.
# A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.

# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.

class Text:
    def __init__(self, text_str):
        self.text_str = text_str

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
        return cls(text_content)

    def word_frequency(self, target_word):
        words = self.text_str.split()
        frequency = words.count(target_word)
        return frequency

    def most_common_word(self):
        words = self.text_str.split()
        if not words:
            return None 
        return max(set(words), key=words.count)

    def unique_words(self):
        words = self.text_str.split()
        return list(set(words))
    

# sample_string = "A good book would sometimes cost as much as a good house."
# text_instance = Text(sample_string)

# freq_word = "book"
# print(f"Frequency of '{freq_word}': {text_instance.word_frequency(freq_word)}")

# most_common = text_instance.most_common_word()
# print(f"Most common word: {most_common}")

# unique_words = text_instance.unique_words()
# print("Unique words:", unique_words) 

text_instance = Text.from_file('the_stranger.txt')
freq_word_text = "the"
print(f"Frequency of '{freq_word_text}': {text_instance.word_frequency(freq_word_text)}")

most_common = text_instance.most_common_word()
print(f"Most common word: {most_common}")

unique_words = text_instance.unique_words()
print("Unique words:", unique_words)

