from collections import Counter

def solution(k, tangerine):
    size_count = Counter(tangerine) # 딕셔너리로 return
    sorted_count = sorted(size_count.values(), reverse=True)
    
    min_count = 0
    total = 0
    
    for count in sorted_count:
        total += count
        min_count += 1
        if total >= k:
            break
    
    return min_count
