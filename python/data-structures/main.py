# import my_module
# imports whole module 

from my_module import foo as bar, person, x
# imports specific modules
# if you sufix with as it removed conflict

# print(my_module)
# prints location

# print(dir(my_module))
# lists modules

def foo(x):
    print(x)

foo(person)
bar({'name': 'Matt', 'age': 51})

# don't need to prefix when importing specific modules


print(dir())