''' ages
user_value = input("What is your age?")
if int(user_value) < 18:
    print("You are a minor")
else:
    print("Drake doesnt want you")

'''

''' doubler

def double(number):
    print (float(number) * 2)

n = input("Which number do you want to double? ")

double(n)

'''

''' calculator

def add(a, b):
    print(int(a) + int(b))

while True:
    a = input("Input two numbers you want to add: ")
    b = input()

    add(a,b)

'''

''' lists

def food(item):
    fav_food.append(item)
    print(fav_food)

fav_food = []

food(input("What's your favorite food? "))
food(input("And another one! "))
food(input("And another one! "))

n = len(fav_food)
print(fav_food[int(n/2)])

'''

''' multiplication table

for i in range(1, 11):
    for j in range(1, 11):
        print (str(i * j) + " ")
    print (" ")

'''

''' Greek
letters = ['alpha','beta','gamma','delta',
'epsilon','zeta','eta']

for i, value in enumerate(letters, 1):
    if (i%3 == 0):
        print (str(value))
'''

''' food
class food:
    def __init__(self, name, carbs, proteins, fats ):
        self.name = name
        self.carbs = carbs
        self.proteins = proteins
        self.fats = fats

    def calories(self):
        return self.carbs*4 + self.proteins*4 + self.fats*9

    def __str__(self):
        return self.name

pasta = food("Pasta", 5,7,9)
print(pasta)

'''

''' user_calculator
def calc(a, b):
    try:
        return a + b
    except TypeError:
        print ("'{}' is not a number".format(a))

print(calc("gd",9))
'''
''' keyword None is used to create a variable with no value
    keyword pass is used to skip a code block
'''

''' Vehicle

class Vehicle:
    def __init__(self):
        raise NotImplementedError("You must use a subclass.")

    def __str__(self):
        return self.name

class Motorcycle(Vehicle):
    def __init__(self):
        self.wheels = 2

class Car(Vehicle):
    def __init__(self):
        self.wheels = 4

print(Car)

'''
''' List comprehensions are a special feature in Python that let us create a list �on the fly�.
The syntax is [what_we_want for thing in iterable if condition]:
� what_we_want: What ends up in the new list. This is
often just the thing in the iterable, but we can modify
the thing if we want.
thing: The object in the iterable.
� iterable: Something that can be passed to a for-each
loop, such as a list, range, or tuple.
� condition: (Optional.) A condition to limit what is
added to the list.

lista = [a for a in range(5) if a < 3]
print(lista)

'''

'''
consumables = []
for item in self.inventory:
    if isinstance(item, Consumables)
'''

''' if not consumables means if consumables list is empty '''





import time
import sys

def type(str):
    for letter in str:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

type("This sentence is typed.")
type("Oh woe the day thy lost thyself!")
