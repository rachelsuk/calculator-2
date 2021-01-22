"""CLI application for a prefix-notation calculator."""
from functools import reduce 

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
while True:
    user_input = input("Please include operator, first number, second number?")
    tokens = user_input.split(',')
    tokens_float = [float(i) for i in tokens[1:]]
    if tokens[0]=="q":
        break
    elif tokens[0]=="+":
        print(add(float(reduce(add, tokens_float[:-1])),tokens_float[-1]))
    elif tokens[0]=="-":
        print(subtract(float(reduce(subtract, tokens_float[:-1])),tokens_float[-1]))
    elif tokens[0]=="*":
        print(multiply(float(reduce(multiply, tokens_float[:-1])),tokens_float[-1]))
    elif tokens[0]=="/":
        print(divide(float(reduce(divide, tokens_float[:-1])),tokens_float[-1]))
    elif tokens[0]=="**":
        print(power(float(reduce(power, tokens_float[:-1])),tokens_float[-1]))
    elif tokens[0]=="%":
        print(mod(float(reduce(mod, tokens_float[:-1])),tokens_float[-1]))
    elif tokens[0]=="**2":
        if len(tokens)==2:
            print(square(float(tokens[1])))
        else:
            print("need to provide only one value when calculating ^2")
    elif tokens[0]=="**3":
        if len(tokens)==2:
            print(cube(float(tokens[1])))
        else:
            print("need to provide only one value when calculating ^3")
    else:
        print("not a valid command, try again")
