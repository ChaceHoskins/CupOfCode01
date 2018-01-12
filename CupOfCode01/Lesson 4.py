i_am = 'chace'
age = 23
print('let us talk about {}.'.format(i_am))

print('{1} {0}'.format('love', 'chocolate', 'test', 'four'))

print('{:_>10}'.format('sucker'))  # choose padding #
print('{:_<10}'.format('sucker'))
print('{:_^10}'.format('sucker'))

x = 'elephant'
print(x[:4])
x = 9-11
print(x)
x = 11-9
print(x)
x = 11-9
print('{:+d}'.format(x)) #integers get a d, floats an f, and yes we can pad numbers#

print('{:06.2f}'.format(3.141592653589793))

data = {'first': 'Hannah', 'last':'Yomama'}
print('{first} {last}'.format(**data))
