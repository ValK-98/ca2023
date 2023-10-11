my_dog = { 'name': 'Ted', 'age': 15, 'breed': 'Border Collie'}
# Key value pairs. 'name' is key - 'Ted' is value.
# A tuple is an immutable list. Has key and value in it

my_dog['age'] = 16
# Can change values
my_dog['owner'] = 'Matt'
# Can add keys

# print(my_dog.items())
# Gives tuples

# for k, v in my_dog.items():
#     print(f'The value of "{k}" is {v}')

# print(item) Gives keys, my_dog[item] gives values

print(my_dog.get('stage', 'Unknown'))

# by using the .get method it returns None rather than error. 