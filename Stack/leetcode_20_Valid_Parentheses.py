"""
Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {'(': ')', '{': '}', '[': ']'}
        stack = ''
        for symbol in s:
            if symbol in hash_map:  # open parentheses
                stack = stack + symbol
            else:  # closing parentheses
                if len(stack) > 0:  # there is open p in stack
                    if hash_map[stack[-1]] == symbol:  # if it is closing
                        stack = stack[:-1]  # del last el from stack
                    else:  # anogher closing
                        return False
                else:  # starts with closing
                    return False
        if stack:
            return False
        else:
            return True
