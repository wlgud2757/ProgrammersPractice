def solution(s):
    number = [int(num) for num in s.split()]
    return f"{min(number)} {max(number)}"
