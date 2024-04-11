def solution(num_list):
    num_pro = 1
    num_sum = 0
    for num in num_list:
        num_pro *= num
        num_sum += num
    return 1 if num_pro < (num_sum * num_sum) else 0
