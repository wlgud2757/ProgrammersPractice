def solution(code):
    mode = 0
    ret = ""
    for idx in range(0, len(code)):
        if code[idx] == "1":
            mode = 0 if mode == 1 else 1
        elif mode == 0 and idx % 2 ==0:
            ret += code[idx]
        elif mode == 1 and idx % 2 != 0:
            ret += code[idx]
    if len(ret) == 0:
        ret = "EMPTY"
    return ret
