from functools import wraps


# ZAD1

#def logged(func):
#    def inner(*args, **kwargs):
#        print(f"You called {func.__name__}{args} it returned {func(*args, **kwargs)}")
#        return func(*args)
#    return inner


#@logged
#def func(*args):
#    return 3 + len(args)

#a = func(2, 2)
#print(2 + a)
#print(a)
#print(func(4, 4, 4))


# ZAD2

#def add_stars(func):
#    def inner(*args, **kwargs):
#        print(kwargs['amount'] * '*')
#        func(*args)
#        print(kwargs['amount'] * '*')

#    return inner


#@add_stars
#def print_text(*args):
#    print(args[0])


#print_text("Hello World", amount=11)


#class Stars:
#    def __init__(self, stars):
#        self.stars = stars

#    def __call__(self, txt):
#        print(self.stars * "*")
#        print(txt)
#        print(self.stars * "*")


#s = Stars(12)
#s("Hello World")
#s.__call__("Hello World")


#class Stars:
#    def __init__(self):
#        pass

#    def __call__(self, txt, stars):
#        print(stars * "*")
#        print(txt)
#        print(stars * "*")

#s = Stars()
#s("Hello World", 10)
#s.__call__("Hello World", 10)


# ZAD3

#def count(func):
#    counts = {}
#    def inner():
#        if func.__name__ in counts:
#            counts[func.__name__] += 1
#        else:
#            counts[func.__name__] = 1
#        func()
#        print(counts)
#    return inner

#@count
#def say():
#    print('Hello')

#@count
#def say_2():
#    print('Hello 2')

#say()
#say()
#say_2()
#say_2()
#say_2()
#say_2()

# ZAD4

#def arg_check(arg):
#    def check(old_func):
#        def new_func(*args):
#            print(isinstance(old_func(*args), arg))
#            return old_func(*args)
#        return new_func

#    return check


#@arg_check(int)
#def add(one, two):
#    return one + two


#print(add(1, 2))

# ZAD5

#import time

#def timethis(func):
#    def inner(*args):
#        start_time = time.time()
#        print(start_time)
#        x = func(*args)
#        end_time = time.time()
#        print(end_time)
#        result = end_time - start_time
#        print('Result in seconds: ', result)
#        return x

#    return inner

#@timethis
#def dodawanie(a, b):
#    time.sleep(5)
#    return a + b

#print(dodawanie(4538, 34848))

# ZAD6

#@property

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def blabla(self):
        print("Get radius")
        return self._radius

    @blabla.setter
    def radius(self, value):
        print("Set radius")
        self._radius = value

    @blabla.deleter
    def radius(self):
        print("Delete radius")
        del self._radius


circle = Circle(42)
print(circle.radius)
circle.radius = 100
print(circle.radius)
del circle.radius


# @abstractmethod

# from abc import ABC, abstractmethod

# class Shape(ABC):

#    @abstractmethod
#    def area(self):
#        pass

# class Rectangle(Shape):

#    def __init__(self, width, height):
#        self.width = width
#        self.height = height

#    def area(self):
#        return self.width * self.height


# rect = Rectangle(10, 20)
# print(rect.area())


# @dataclass
# class Person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age


# from dataclasses import dataclass

# @dataclass
# class Person:
#    name: str
#    age: int


# p1 = Person('Paulina', 35)
# print(p1)


# @classmethod, @staticmethod

# from datetime import date


# class Person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    @classmethod
#    def fromBirthYear(cls, name, year):
#        return cls(name, date.today().year - year)

#    @staticmethod
#    def isAdult(age):
#        return age > 18


# person1 = Person('Paulina', 35)
# person2 = Person.fromBirthYear('Paulina', 1940)

# print(person1.age)
# print(person2.age)
# print(Person.isAdult(22))
