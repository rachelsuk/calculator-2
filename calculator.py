"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
while True:
    user_input = input("Please include operator, first number, second number?")
    tokens = user_input.split(',')
    if tokens[0]=="q":
        break

    if len(tokens) == 3:
        if tokens[0]=="+":
            print(add(float(tokens[1]), float(tokens[2])))
        elif tokens[0]=="-":
            print(subtract(float(tokens[1]), float(tokens[2])))
        elif tokens[0]=="*":
            print(multiply(float(tokens[1]), float(tokens[2])))
        elif tokens[0]=="/":
            print(divide(float(tokens[1]), float(tokens[2])))
        elif tokens[0]=="**":
            print(power(float(tokens[1]), float(tokens[2])))
        elif tokens[0]=="%":
            print(mod(float(tokens[1]), float(tokens[2])))
        else: 
            print ("not a valid command")
    elif len(tokens) == 2: 
        if tokens[0]=="**2":
            print(square(float(tokens[1])))
        elif tokens[0]=="**3":
             print(cube(float(tokens[1])))
        else: 
            print("not a valid command")
    else:
        print("not a valid command, try again")
