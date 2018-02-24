# The code in this file is taken from 
# Python for Everybody, by Charles Severance at www.py4e.com
# Thank you, Dr. Chuck

# A value is one of the basic things a program works with, like a letter 
# or a number
# Chapter 4
# Functions
# Function arguments, return values
# Passing arguments to a function
type(32)

# Built-in functions
max('Hello world')
# Try help(max) or in IPython, max?
min('Hello world')
len('Hello world')

# Type conversion functions
int('32')
int('Hello')

int(3.99999)
int(-2.3)

float(32)
float('3.14159')

str(32)
str(3.14159)

# Random numbers
# Explain import, namespaces!
import random
for i in range(10):
    x = random.random()
    print(x)

# Try random.[tab complete] or dir(random)
random.randint(5, 10)
random.randint(5, 10)
t = [1, 2, 3]
random.choice(t)

# Math functions
import math
print(math)

signal_power, noise_power = 30.0, 1.45
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
radians = 0.7
height = math.sin(radians)

degrees = 45
radians = degrees / 360.0 * 2 * math.pi
math.sin(radians)

math.sqrt(2) / 2.0


# Adding new functions
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
	
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
	
print(print_lyrics)
print(type(print_lyrics))

print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
	
repeat_lyrics()

# Function definitions must come before they are called in a script
# However, the statements inside a function definition do not execute
# until the function is called!

# Parameters and arguments
def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice('Spam')
print_twice(17)
print_twice(math.pi)

print_twice('Spam '*4)

michael = 'Eric, the half a bee.'


x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2

math.sqrt(5)
result = print_twice('Bing')
print(result)

print(type(None))

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)


# Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
# Score   Grade
# > 0.9     A
# > 0.8     B
# > 0.7     C
# > 0.6     D
# <= 0.6    F
# Program Execution:
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F

# CHAPTER 5 = ITERATION

x = 0
x = x + 1

# While loop
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')

# Infinite loops, break, and continue
n = 10
while True:
    print(n, end=' ')
    n = n - 1
print('Done!')

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')


# For loops
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count: ', count)

total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Total: ', total)


# Maximum and minimum loops
largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)

smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)

def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest
