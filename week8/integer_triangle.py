def solution(triangle):
    height = len(triangle)
    
    for i in range(1, height):
        for j in range(i+1):
            if j == 0:
                left_up = 0
            else:
                left_up = triangle[i-1][j-1]
            if j == i:
                up = 0
            else:
                up = triangle[i-1][j]
            triangle[i][j] += max(left_up, up)
    
    return max(triangle[-1])
