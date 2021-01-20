"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
while True:
    user_input = input("Please include operator, first number, second number?")
    tokens = user_input.split(',')
    if tokens[0]=="q":
        break
    elif tokens[0]=="+":
        print(add(int(tokens[1]), int(tokens[2])))
    elif tokens[0]=="-":
        print(subtract(int(tokens[1]), int(tokens[2])))
    elif tokens[0]=="*":
        print(multiply(int(tokens[1]), int(tokens[2])))
    elif tokens[0]=="/":
        print(divide(int(tokens[1]), int(tokens[2])))
    elif tokens[0]=="**2":
        print(square(int(tokens[1]), int(tokens[2])))
    elif tokens[0]=="**3":
        print(cube(int(tokens[1]), int(tokens[2])))
    elif tokens[0]=="**":
        print(power(int(tokens[1]), int(tokens[2])))
    elif tokens[0]=="%":
        print(mod(int(tokens[1]), int(tokens[2])))
