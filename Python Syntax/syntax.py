""" 
## variables (number)
a = 2
b = 3
print(a+b)

## Variables ( text )

a_string = "like this"
print(string)

# Variables( float )

a_float = 3.12
print(a_float)

# Boolean

a = True
b = False
print(a, b)

# None
a_none = None
print(a_none)


# List
# 변경 가능
days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(type(days))

# Tuple
# 변경 불가
days = ("Mon", "Tue", "Wed", "Thur", "Fri")
print(days)

# Dictionary

nico = {
    "name": "Nico",
    "age": 29,
    "korean": True,
    "fav_food": ["Kimchi", "Sashimi"]
}

print(nico)
nico["handsome"] = True
print(nico)

# function

# How to define function

def say_hello(who):
    print("Hello!", who)

say_hello('Nico')

# Practice function

def plus(a, b):
    return a + b

def minus(a, b=0):
    return a - b

def multiply(a, b):
    return a * b

print(plus(2, 3))
print(minus(2))

# function keyworded Arguments

def plus(a, b):
    return a + b

result = plus(b=30, a=1)

print(result)

# format

def say_hello(name, age):
    return f"Hello {name} you are {age} years old"


hello = say_hello("nico", "12")
print(hello)

# Calculator


def plus(a, b):
    return int(a) + int(b)


def minus(a, b):
    return int(a) - int(b)


def multiply(a, b):
    return int(a) * int(b)


def divide(a, b):
    return int(a) / int(b)


def remind(a, b):
    return int(a) % int(b)


def power(a, b):
    return int(a) ** int(b)


print(plus("10", 2))
print(minus("10", 2))
print(multiply("10", 2))
print(divide("10", 2))
print(remind("10", 2))
print(power("10", 2))


# if else and or
# age check


def age_check(age):
    print(f"you are {age}")
    if age < 18:
        print("you can drink")
    elif age == 18 or age == 19:
        print("you are new to this!")
    elif age > 20 and age < 25:
        print("you are still kind of young")
    else:
        print("enjoy your drink")


age_check(18)

# for loop

import ceil from math
days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for i in days:
    if i is "Wed":
        break
    else:
        print(i)

# how to import module
from math import ceil, fsum
print(ceil(13.2))
print(fsum([1, 2, 3, 4]))
"""
