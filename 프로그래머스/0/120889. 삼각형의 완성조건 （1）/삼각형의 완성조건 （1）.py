def solution(sides):
    sides.sort()
    a = sides[0] + sides[1]
    if sides[2] < a:
        answer = 1
    else:
        answer = 2
    return answer