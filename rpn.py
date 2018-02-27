#!/usr/bin/env python3

import operator
import extras_operators

operators = {
    '+': {
        'function': operator.add,
        'type': "binary",
    },
    '-': {
        'function': operator.sub,
        'type': 'binary',
    },
    '*': {
        'function': operator.mul,
        'type': 'binary'
    },
    '/': {
        'function': operator.truediv,
        'type': 'binary'
    },
    '//': {
        'function': operator.floordiv,
        'type': 'binary'
    },
    '^': {
        'funciton': operator.pow,
        'type': 'binary'
    },
    '&': {
        'function': operator.and_,
        'type': 'binary',
    },
    '|': {
        'function': operator.or_,
        'type': 'binary',
    }
}

def calculate(myarg, output=True):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)

        except ValueError:
            function = operators[token]['function']
            arg2 = stack.pop()

            if operators[token]['type'] == 'binary':
                arg1 = stack.pop()
                stack.append(function(arg1, arg2))
            else:
                stack.append(function(arg2))

        if output:
            print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()

