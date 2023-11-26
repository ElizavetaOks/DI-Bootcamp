#Ex 1
print('Hello world \n'*4)

#Ex 2
a = 99**3*8
print(a)

#Ex 3
#False
#True
#Error
#Error
#False

#Ex 4
computer_brand = 'Lenovo'
print(f'I have a {computer_brand} computer')

#Ex 5
name = 'Elizaveta'
age = 36
shoe_size = 36
info = f'My name is {name}. I am {age}. I have {shoe_size} size of shoes.'
print(info)

#Ex 6
a = 57
b = 14
if a>b:
    print('Hello World')

#Ex 7
a = int(input('Give me any number '))
if a%2 == 0:
    print('Number is odd')
else:
    print('Number is even')

#Ex 8
your_name = input('What is your name? ')
if your_name == 'Elizaveta':
    print('You are like a Queen')
else:
    print('It could be worse')

#Ex 9
height = int(input('Tell me your height in inches '))
height_in_sm = height*2.54
if height_in_sm > 145:
    print('You are tall enough to ride')
else:
    print('You need to grow some more to ride')
