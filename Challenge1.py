#Ex 1
st = input('Write any string ')
if len(st) < 10:
    print('String is not long enough')
elif len(st) > 10:
    print('String is too long')
else:
    print('Perfect string')

#Ex 2
print(st[0], st[-1])

#Ex 3
x = input('Enter a string ')
for i in range(len(x)):
    print(x[:i+1])

#Ex 4
import random
st = list(input('Enter a string '))
random.shuffle(st)
print(''.join(st))
