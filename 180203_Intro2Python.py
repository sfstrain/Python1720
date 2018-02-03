# A value is one of the basic things a program works with, like a letter 
# or a number
print(4)

#These values belong to different types
type('Hello, World!')
type(17)
type(3.2)
type('17')
type('3.2')


print(1,000,000)

# A variable is a name that refers to a value.
# An assignment statement creates new variables and gives them values:
message = 'And now for something completely different'
n = 17
pi = 3.1415926535897931
print(n)
print(pi)
type(message)
type(n)
type(pi)

# Variable names can be arbitrarily long. They can contain both letters 
# and numbers, but they cannot start with a number.
76trombones = 'big parade'
more@ = 1000000
class = 'Advanced Theoretical Zymurgy'
# It turns out that class is one of Python's keywords. 
# Python reserves 33 keywords:
# and       del       from      None      True
# as        elif      global    nonlocal  try
# assert    else      if        not       while
# break     except    import    or        with
# class     False     in        pass      yield
# continue  finally   is        raise
# def       for       lambda    return

# A statement is a unit of code that the Python interpreter can execute. 
print(1)
x = 2
print(x)
# The assignment statement produces no output.

# Operators are special symbols that represent computations like addition 
# and multiplication. The values the operator is applied to are called operands.
# The operators +, -, *, /, and ** perform addition, subtraction, multiplication, 
# division, and exponentiation.

# An expression is a combination of values, variables, and operators. 
first = 10
second = 15
print(first+second)

first = '100'
second = '150'
print(first + second)

inp = input()
print(inp)
name = input('What is your name?\n')
print(name)

prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
speed = input(prompt)
print(speed + 5)

===================================

5 == 5
5 == 6
type(True)
type(False)

      x != y               # x is not equal to y
      x > y                # x is greater than y
      x < y                # x is less than y
      x >= y               # x is greater than or equal to y
      x <= y               # x is less than or equal to y
      x is y               # x is the same as y
      x is not y           # x is not the same as y

# There are three logical operators: and, or, and not.

x > 0 and x < 10
n%2 == 0 or n%3 == 0
not (x > y)

# Conditional statements give us the ability to check conditions and change 
# the behavior of the program accordingly

if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
    
if choice == 'a':
    print('Bad guess')
elif choice == 'b':
    print('Good guess')
elif choice == 'c':
    print('Close, but not correct')

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
