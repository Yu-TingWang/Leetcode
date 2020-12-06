"""
https://leetcode.com/problems/valid-parentheses/
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
---------------------------------------------------
https://leetcode.com/problems/longest-valid-parentheses/
32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed)
parentheses substring.
---------------------------------------------------

"""
def isValid(s:str):
    d = {'}':'{',']':'[',')':'('}
    stack = []
    for e in s:
        if e in d.values():
            stack.append(e)
        elif e in d.keys():
            if stack==[] or stack.pop()!=d[e]:
                return False
        else:
            return False
    return stack == []

if __name__ == '__main__':
    s = '()'
    print(isValid(s))