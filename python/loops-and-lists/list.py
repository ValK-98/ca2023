spam = ['cat', 'dog', 'bird']
eggs = [12, 78, 100, 54, 42]
foo = ['Mat', 51]
tic_tac_toe = [
    ['','o',''],
    ['x', 'o', ''],
    ['','x', '']
    ]


# for index in range(len(spam)): 
#     print(spam[index])

# for index, animal in enumerate(spam): 
#     print(f'{index + 1}. {animal}')

# print(list(range(1, 10, 2)))

# or .extend(foo)
# or spam += foo

# spam.append('kangaroo')
# print(spam)

# x = spam.index('dog')
# print(x)

# def display_person(person):
#     print(f'{person[0]} is {person[1]} years old and {person[2]} cm tall')

# def display_person(person):
#     # name = person[0]
#     # age = person[1]
#     # height = person[2]
#     name, age, height = person
#     print(f'{name} is {age} years old and {height} cm tall')


spam.insert(1, 'kangaroo')
print(spam)