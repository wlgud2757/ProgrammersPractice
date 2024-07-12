def solution(s):
    stack = []
    
    for alphabet in s:
        if len(stack) != 0 and stack[-1] == alphabet:
            stack.pop()
        else:
            stack.append(alphabet)
    
    return 1 if not stack else 0
