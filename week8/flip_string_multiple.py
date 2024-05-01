def solution(my_string, queries):
    result = my_string
    for query in queries:
        temp = list(result[query[0]:query[1]+1])
        temp.reverse()
        temp = "".join(temp)
        result = list(result)
        result[query[0]:query[1]+1] = temp
        result = "".join(result)
    return result
