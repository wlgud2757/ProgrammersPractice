def solution(n, k):
    answer = []
    count = 1
    while True:
        if k * count <= n:
            answer.append(k * count)
            count += 1
        else:
            break
    return answer
