def solution(arr):
    answer = []
    for item in arr:
        if item >= 50 and item % 2 == 0:
            answer.append(item / 2)
        elif item < 50 and item % 2 != 0:
            answer.append(item * 2)
        else:
            answer.append(item)
    return answer
