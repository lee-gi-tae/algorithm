def solution(a, b):
    hab = str(a) + str(b)
    gop = 2 * a * b
    if int(hab) >= gop:
        return int(hab)
    else:
        
        return gop