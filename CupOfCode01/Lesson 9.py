x = 5
y = 8

if x > y:
    print('x is greater than y')

if x < y:
    print('x is LESS than y')

while x < y:
    print('x is LESS than y')
    x += 1
print('\n')
x = 5
y = 8
z = 3

if z < x < y:
    print('Now we are comparing three variables')

if x > y:
    print('x is greater')
elif x < 100:
    print('it is not greater than 100')
else:
    print('x is not greater')