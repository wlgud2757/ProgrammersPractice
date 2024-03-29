def solution(n, control):
    for operation in control:
        if operation == 'w':
            n += 1
        elif operation == 's':
            n -= 1
        elif operation == 'd':
            n += 10
        else:
            n -= 10
    return n
