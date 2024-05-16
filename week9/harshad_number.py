def solution(x):
    array = list(str(x))
    array = [int(num) for num in array]
    
    digit = 0
    for num in array:
        digit += num
    
    return True if int(x) % digit == 0 else False
