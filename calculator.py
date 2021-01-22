"""CLI application for a prefix-notation calculator."""
from functools import reduce 

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
def my_reduce(function, numbers):
    value = numbers[0]
    for i in range(len(numbers)-1):
        value = function(value,numbers[i+1])
    return float(value)

input_file = open("calculator-2_input.txt")
output_file = open("calculator-2_output.txt", "w")

for line in input_file:
    tokens = line.split(',')
    tokens_float = [float(i) for i in tokens[1:]]
    if tokens[0]=="q":
        break
    elif tokens[0]=="+":
        result = add(my_reduce(add, tokens_float[:-1]),tokens_float[-1])
    elif tokens[0]=="-":
        result = subtract(my_reduce(subtract, tokens_float[:-1]),tokens_float[-1])
    elif tokens[0]=="*":
        result = multiply(my_reduce(multiply, tokens_float[:-1]),tokens_float[-1])
    elif tokens[0]=="/":
        result = divide(my_reduce(divide, tokens_float[:-1]),tokens_float[-1])
    elif tokens[0]=="**":
        result = power(my_reduce(power, tokens_float[:-1]),tokens_float[-1])
    elif tokens[0]=="%":
        result = mod(my_reduce(mod, tokens_float[:-1]),tokens_float[-1])
    elif tokens[0]=="**2":
        if len(tokens)==2:
            result = square(float(tokens[1]))
        else:
            result = "need to provide only one value when calculating ^2"
    elif tokens[0]=="**3":
        if len(tokens)==2:
            result = cube(float(tokens[1]))
        else:
            result = "need to provide only one value when calculating ^3"
    else:
        result = "not a valid command, try again"

    if type(result) == float:
        output_file.write("{:.2f}".format(result) + "\n")
    else:
        output_file.write(result + "\n")
output_file.close()

