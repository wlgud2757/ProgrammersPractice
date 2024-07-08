def solution(numbers, target):
    def dfs(index, total):
        # 종료 조건
        if index == len(numbers):
            return 1 if total == target else 0
        
        # 더하거나 빼거나 둘 중에 하나
        adding = dfs(index + 1, total + numbers[index])
        subtracting = dfs(index + 1, total - numbers[index])
        
        # target number가 된 case 횟수를 다 더함
        return adding + subtracting
    
    # 처음에는 첫번째 숫자와 합이 0이 된 상태에서 시작
    return dfs(0, 0)
