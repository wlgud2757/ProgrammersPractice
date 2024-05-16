def solution(s):
    if s[0] == ')' or s[-1] != ')':
        return False
    
    stack = []
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        elif not stack or stack.pop() != '(':
                return False
    
    return True if len(stack) == 0 else False
