def solution(n):
    answer = 0
    odd_or_even = n % 2
    
    for num in range(odd_or_even, n + 1, 2):
        if odd_or_even == 1:
            answer += num
        else:
            answer += num ** 2
            
    return answer
