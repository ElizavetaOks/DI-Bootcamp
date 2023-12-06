# Exercise 1: Currencies

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __int__(self):
        return self.amount
    
    def __repr__(self):
        return f"{self.amount} {self.currency}s"

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
        elif isinstance(other, (int, float)):
            return Currency(self.currency, self.amount + other)
        else:
            raise TypeError("Unsupported operand type")

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.amount += other
            return self
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
            return self
        else:
            raise TypeError("Unsupported operand type")
              
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))   # '5 dollars'
print(int(c1))   # 5
print(repr(c1))  # '5 dollars'
print(c1 + 5)    # 10
print(c1 + c2)   # 15

print(c1)        # 5 dollars

c1 += 5
print(c1)        # 10 dollars

c1 += c2
print(c1)        # 20 dollars
              
#print(c1 + c3)   # TypeError: Cannot add between Currency type <dollar> and <shekel>


# Exercise 3: String Module
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

import random
import string

def gen_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

random_string = gen_random_string(5)
print(random_string)


# Exercise 4 : Current Date
# Create a function that displays the current date.
# Hint : Use the datetime module.

from datetime import datetime

def display_current_date():
    current_date = datetime.now().strftime("%d-%m-%Y")
    print(current_date)

display_current_date()

# Exercise 5 : Amount Of Time Left Until January 1st
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

from datetime import datetime, timedelta

def time_until_january_first():
    current_datetime = datetime.now()
    target_date = datetime(current_datetime.year + 1, 1, 1)
    time_difference = target_date - current_datetime
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"The 1st of January is in {days} days and {hours:02}:{minutes:02}:{seconds:02} hours.")

time_until_january_first()


# Exercise 6 : Birthday And Minutes
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

from datetime import datetime

def minutes_lived(birthdate):
    birthdate_datetime = datetime.strptime(birthdate, "%d-%m-%Y")
    current_datetime = datetime.now()

    minutes_lived = (current_datetime - birthdate_datetime).total_seconds() / 60

    print(f"You have lived for {int(minutes_lived):,} minutes.")

birthdate_input = input("Enter your birthdate (DD-MM-YYYY): ")
minutes_lived(birthdate_input)


# Exercise 7 : Faker Module
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.

from faker import Faker

fake = Faker()
users = []

def add_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code(),
    }
    users.append(user)

for _ in range(5):
    add_user()

for user in users:
    print(user)
