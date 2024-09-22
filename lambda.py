# Used for Anonymous Functions.
'''

An anonymous function in Python is a function without a name. 
It can be immediately invoked or stored in a variable. 
Anonymous functions in Python are also known as lambda functions.
A lambda function can take any number of arguments, but can only have one expression.

'''

def examplefunc(n):
    return lambda e: n * e

doubler = examplefunc(2)

print(doubler(8))

# Lets put it into action

def func(n):
    return lambda x: n * x

doubler = examplefunc(2)
tripler = examplefunc(3)
quadrupler = examplefunc(4)

print(doubler(int(input("What Number would you like to double? Enter here: "))))
print(tripler(int(input("What Number would you like to triple? Enter here: "))))
print(quadrupler(int(input("What Number would you like to quadruple? Enter here: "))))