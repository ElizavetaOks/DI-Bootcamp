# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

word = input("Enter a word: ")

letter_dict = {}
for index, letter in enumerate(word):
    if letter in letter_dict:
        letter_dict[letter].append(index)
    else:
        letter_dict[letter] = [index]
print(letter_dict)

# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.

items_purchase = {
  "Water": 1,
  "Bread": 3,
  "TV": 1000,
  "Fertilizer": 20
}

wallet = 300
affordable_items = [item for item, price in items_purchase.items() if price <= wallet]
sorted_affordable_items = sorted(affordable_items)

if not sorted_affordable_items:
    print("Nothing")
else:
    print("Items you can afford:", sorted_affordable_items)
