def solution(a, d, included):
    answer = 0
    for flag in included:
        if flag is True:
            answer += a
        a += d
    return answer
