# Challenge 1 : Sorting
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension

sequence = input('Enter comma-separated sequence of words: ')
words = [word.strip() for word in sequence.split(',')]
sorted_words = sorted(words)

print(', '.join(sorted_words))


# Challenge 2 : Longest Word
# Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
# Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).

from functools import reduce
sentence = "Forgetfulness is by all means powerless!"
word = sentence.split()
longest_word = str()
for i in word:
    if len(i) > len(longest_word):
        longest_word = i
    
print(longest_word)

