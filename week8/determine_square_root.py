import math

def solution(n):
    square_root = int(math.sqrt(n))
    if square_root**2 == n:
        return (square_root+1)**2
    else:
        return -1
