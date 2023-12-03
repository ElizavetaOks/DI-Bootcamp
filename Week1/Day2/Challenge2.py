# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.

number = int(input("Enter a number: "))
length = int(input("Enter the desired length of the list: "))
multiples_list = []
for i in range(1, length+1):
     multiples_list.append(number * i)
print(multiples_list)


# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

user_string = input("Enter a string: ")
final_string = ""
for i in range(len(user_string)):
    if i == 0 or user_string[i] != user_string[i - 1]:
        final_string += user_string[i]
print(final_string)
