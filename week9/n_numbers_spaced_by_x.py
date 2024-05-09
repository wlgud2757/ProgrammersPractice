def solution(x, n):
    answer = [0]
    for i in range(n):
        answer.append(answer[-1] + x)
    answer.pop(0)
    return answer
