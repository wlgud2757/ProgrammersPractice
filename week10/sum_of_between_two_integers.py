def solution(a, b):
    given = [a, b]
    numbers = [num for num in range(min(given), max(given) + 1)]
    return sum(numbers)
