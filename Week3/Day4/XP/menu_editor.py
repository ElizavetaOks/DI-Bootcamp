# Create a file called menu_editor.py , which will have the following functions:
# show_user_menu() - this function should display the program menu (not the restaurant menu!), and ask the user to :
# View an Item (V)
# Add an Item (A)
# Delete an Item (D)
# Update an Item (U)
# Show the Menu (S)
# Call the appropriate function that matches the user’s input.


# class MenuItem:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def update_item(self, new_name, new_price):
#         self.name = new_name
#         self.price = new_price
import psycopg2
from menu_manager import MenuManager

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def update_item(self, new_name, new_price):
        self.name = new_name
        self.price = new_price

class MenuEditor:
    def __init__(self):
        self.menu = []

    def show_user_menu(self):
        print("===== Menu Editor =====")
        print("V - View an Item")
        print("A - Add an Item")
        print("D - Delete an Item")
        print("U - Update an Item")
        print("S - Show the Menu")
        print("E - Exit")

        choice = input("Enter your choice: ").upper()

        if choice == 'V':
            self.view_item()
        elif choice == 'A':
            self.add_item_to_menu()
        elif choice == 'D':
            self.remove_item_from_menu()
        elif choice == 'U':
            self.update_item_from_menu()
        elif choice == 'S':
            self.show_restaurant_menu()
        elif choice == 'E':
            self.show_restaurant_menu()
            print("Exiting program.")
            exit()
        else:
            print("Invalid choice. Please try again.")
            self.show_user_menu()

# add_item_to_menu() - this function should ask the user to input the item’s name and price. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
# If the item was added successfully print a message which states: item was added successfully.
            
    def add_item_to_menu(self):
        name = input("Enter the item's name: ")
        price = float(input("Enter the item's price: "))
        new_item = MenuItem(name, price)
        self.menu.append(new_item)
        print(f"{name} was added successfully.")

# remove_item_from_menu()- this function should ask the user to input the name of the item they want to remove from the restaurant’s menu. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
# If the item was deleted successfully – print a message to let the user know this was completed.
# If not – print a message which states that there was an error.

    def remove_item_from_menu(self):
        name = input("Enter the name of the item to remove: ")
        for item in self.menu:
            if item.name.lower() == name.lower():
                self.menu.remove(item)
                print(f"{name} was deleted successfully.")
                return
        print("Error: Item not found.")

# update_item_from_menu()- this function should ask the user to input the name and price of the item they want to update from the restaurant’s menu, as well as to input the name and price they want to change them with. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
# If the item was updated successfully – print a message to let the user know this was completed.
# If not – print a message which states that there was an error.

    def update_item_from_menu(self):
        name = input("Enter the name of the item to update: ")
        new_name = input("Enter the new name: ")
        new_price = float(input("Enter the new price: "))
        for item in self.menu:
            if item.name.lower() == name.lower():
                item.update_item(new_name, new_price)
                print(f"{name} was updated successfully.")
                return
        print("Error: Item not found.")

# show_restaurant_menu() - print the restaurant’s menu.
    def show_restaurant_menu(self):
        print("===== Restaurant Menu =====")
        for item in self.menu:
            print(f"{item.name}: ${item.price:.2f}")

# Main program loop
if __name__ == "__main__":
    menu_editor = MenuEditor()

while True:
    menu_editor.show_user_menu()
