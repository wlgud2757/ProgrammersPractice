def solution(n):
    bin_one_cnt =  bin(n).count('1')
    while True:
        n += 1
        if bin(n).count('1') == bin_one_cnt:
            return n
