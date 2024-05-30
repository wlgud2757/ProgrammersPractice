def solution(strings, n):
    index = [item[n] for item in strings]
    pair = sorted(zip(index, strings))
    _, answer = zip(*pair)
    return list(answer)
