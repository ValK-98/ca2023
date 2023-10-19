def my_decorator(spam, num):
    def inner_function():
        if num == 42:
            spam('Life, the universe and everything!')
        else:
            spam()

        # name = input('Enter name: ')
        # func(name)

    return inner_function

@my_decorator(num=42) 
def greet(name):
    print(f'Hello, {name}!')


greet()
# my_function()