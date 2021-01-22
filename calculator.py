"""CLI application for a prefix-notation calculator."""
from functools import reduce 

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
def my_reduce(function, numbers):
    value = numbers[0]
    for i in range(len(numbers)-1):
        value = function(value,numbers[i+1])
    return value

while True:
    user_input = input("Please include operator, first number, second number?")
    tokens = user_input.split(',')
    tokens_float = [float(i) for i in tokens[1:]]
    if tokens[0]=="q":
        break
    elif tokens[0]=="+":
        print(add(float(my_reduce(add, tokens_float[:-1])),tokens_float[-1]))
    elif tokens[0]=="-":
        print(subtract(float(my_reduce(subtract, tokens_float[:-1])),tokens_float[-1]))
    elif tokens[0]=="*":
        print(multiply(float(my_reduce(multiply, tokens_float[:-1])),tokens_float[-1]))
    elif tokens[0]=="/":
        print(divide(float(my_reduce(divide, tokens_float[:-1])),tokens_float[-1]))
    elif tokens[0]=="**":
        print(power(float(my_reduce(power, tokens_float[:-1])),tokens_float[-1]))
    elif tokens[0]=="%":
        print(mod(float(my_reduce(mod, tokens_float[:-1])),tokens_float[-1]))
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
