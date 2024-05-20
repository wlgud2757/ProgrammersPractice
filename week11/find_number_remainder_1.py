def solution(n):
    for m in range (1, n):
        if n % m == 1:
            return m
