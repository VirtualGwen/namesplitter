name= input()

splitName = name.split(' ')

if len(splitName) > 2:
    print('{}, {}.{}.'.format(splitName[2], splitName[0][0], splitName[1][0]))
else:
    print('{}, {}.'.format(splitName[1], splitName[0][0]))
