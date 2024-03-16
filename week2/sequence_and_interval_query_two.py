def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        sample = arr[s:e+1]
        min = float("inf")
        for element in sample:
            if element > k and element <= min:
                min = element
        if min not in arr:
            min = -1
        answer.append(min)
    return answer
