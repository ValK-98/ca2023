def my_decorator(spam, num):
    def inner_function():
        if num == 42:
            spam('Life, the universe and everything!')
        else:
            spam()

        # name = input('Enter name: ')
        # func(name)

    return inner_function

# @my_decorator(num=42) 
# def greet(name):
#     print(f'Hello, {name}!')


# greet()
# my_function()

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __add__(self, other): 
        return Point(self.x + other.x, self.y + other.y)

    def __eq__ (self, other) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __repr__(self) -> str:
        return f'Point({self.x}, {self.y})'
    
    def __str__(self) -> str:
        return f' x: {self.x}, y: {self.y}'

p1 = Point(1,2)
p2 = Point(2,3)

print(p1 == p2)

p1 += p2 
print(repr(p1))

# print((p1 + p2).__dict__)