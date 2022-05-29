import  math

course = '''
   what is your name
   are you fine and worth living 
'''
print(course)
x = 2.9
print(round(x))
print(math.ceil(2.9))

is_hot = False
is_cold = False
if is_hot:
    print('it"s a hot day')
    print('Drink plenty water')
elif is_cold:
    print('It is a cold day')
    print('Wear warm clothes')
else:
    print('It is a wonder day')

name = 'wilsom'
if len(name) < 4:
    print('name is too long')
elif len(name) > 10:
    print('name is too long')
else:
    print('good')

    weight = int(input('Weight: '))
    unit = input('(L)s or (K)g')
    if unit.upper() == 'L':
        converted_Weigth = weight * 0.45
        print(f'you are {converted_Weigth}')
    else:
        converted_Weigth = weight / 0.45
        print(f'you are {converted_Weigth}' )