def solution(v):
    given_x = [v[0][0], v[1][0], v[2][0]]
    given_y = [v[0][1], v[1][1], v[2][1]]
    
    new_x = [x for x in given_x if given_x.count(x) == 1][0]
    new_y = [y for y in given_y if given_y.count(y) == 1][0]

    return [new_x, new_y]
