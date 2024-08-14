def solution(s):
    count = 0
    total_removed = 0

    while s != "1":
        removed = s.count('0')
        total_removed += removed
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        count += 1
    
    return [count, total_removed]
