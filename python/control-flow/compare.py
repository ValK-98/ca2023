# x = int(input('What is X? '))
# y = int(input('What is Y? '))


# if x < y : 
#     print('x is less than y') 

# elif x > y:
#     print('x is greater than y') 

# elif x == y: 
#     print('x is equal to y')


# score =int(input('Score: '))

# if score >= 90:
#     print('HD') 
# elif score >= 80:
#     print('D')   
# elif score >= 70: 
#     print('CR')
# elif score >= 50:
#     print('P')
# else: 
#     print('F')

name = input('What is your name? ')

# if name == 'Harry' or 'Ron' or 'Hermoine':
#     print('Gryffindor')
# elif name == 'Draco':
#     print('Slytherin')
# else:
#     print('Mudblood!')

match name :
    case 'Harry' | 'Ron' | 'Hermoine':
        print('Gyffindor')
    case 'Draco':
        print('Slytherin')
    case _:
        print('Mudblood!')