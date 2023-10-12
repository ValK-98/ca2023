# my_dog = {'name': 'Ted', 'age' : 15, 'breed': 'Border Collie'}

# def create(name, age, breed):
#     new_dog = {
#         'name': name,
#         'age': age,
#         'breed': breed,
#         'walks': 0
#     }
#     return new_dog

# def walk(dog){
#     dog['walks'] += 1
# }


class Dog: 
    def greet(self):
        # print(f'spam: {self}')
        print(f'Hello! {self.name}')