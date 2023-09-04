"""
You are given an array of strings tokens
that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer
that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(v1+v2)
            elif token == '-':
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(v1-v2)
            elif token == '*':
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(v1*v2)
            elif token == '/':
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(int(v1/v2))
            else:
                stack.append(int(token))
        return stack[0]
