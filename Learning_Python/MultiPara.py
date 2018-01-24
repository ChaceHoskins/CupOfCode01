def multipara(name, last):
    print('Your first name is ' + name + ' your last name is ' + last)
    if name == 'Chace' or name == 'chace':
        print("Whoa, you're a nerd!")
        print("You're name has " + str(len(name)) + str(len(name)) + ' characters.')
    elif name == 'Jenny' or name == 'jenny':
        print("You're my wife")
        print("You're name has " + str(len(name)) + str(len(name)) + 'characters.')
    else:
        print('Wtf are you running this for')

multipara('Chace', 'Hoskins')

