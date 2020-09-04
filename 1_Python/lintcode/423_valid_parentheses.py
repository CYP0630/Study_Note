
"""
@param s: A string
@return: whether the string is a valid parentheses
"""
def isValidParentheses(self, s):
    # write your code here
    stack = []
    for ch in s:
        if ch == '{' or ch == '[' or ch == '(':
            stack.append(ch)
        else:
                
            if not stack:
                return False
                
            if ch == ']' and stack[-1] != '[' or ch == '}' and stack[-1] != '{' and stack[-1] != '(':
                return False
                
            stack.pop()
                
    return not stack

