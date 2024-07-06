def solution(s):
    s = s.lower()
    word = s.split(' ')
    answer = []
    for case in word:
        answer.append(case.capitalize())
    return ' '.join(answer)
