def firstFunction(name):
    print('Your name is: ' + name)

def getname():
    name = input('What is your name: ')
    return name

def runit():
    print('Booting program')
    firstFunction(getname())

runit()


