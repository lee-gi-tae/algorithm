def solution(a, b):
    c = str(a) + str(b)
    d = str(b) + str(a)
    answer = max(int(c), int(d))
    return answer