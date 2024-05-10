def solution(people, limit):
    people.sort(reverse=True)
    
    boat = 0
    last_idx = len(people) - 1
    for idx, person in enumerate(people):
        # 탈 사람이 없는 경우
        if last_idx < idx:
            break
        # 혼자만 남은 경우
        elif last_idx == idx:
            boat += 1
            break
        # 두 명이서 탈 수 있는 경우
        elif person + people[last_idx] <= limit:
            boat += 1
            last_idx -= 1
        # 혼자 타야하는 경우
        else:
            boat += 1
    
    return boat
