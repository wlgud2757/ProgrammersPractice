def solution(n):
    answer = [int(num) for num in str(n)]
    answer.sort(reverse=True)
    answer = ''.join(map(str, answer))
    return int(answer)
