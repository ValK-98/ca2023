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

# name = input('What is your name? ')

# if name == 'Harry' or 'Ron' or 'Hermoine':
#     print('Gryffindor')
# elif name == 'Draco':
#     print('Slytherin')
# else:
#     print('Mudblood!')

# match name :
#     case 'Harry' | 'Ron' | 'Hermoine':
#         print('Gyffindor')
#     case 'Draco':
#         print('Slytherin')
#     case _:
#         print('Mudblood!')


# Write a Python program to calculate and 
# display the surface area of a user-chosen geometric shape. 
# The 3 possible choices are a square, a circle and a triangle.
a = 0
b = 0
h = 0
r = 0
triangle_area = float(0.5 * b * h)
square_area = float(a**2)
circle_area = float(3.14 * r**2)

if input('Square, circle or triangle? ').lower() == "square":
    a = input('Length of side: ')
    print(square_area)
