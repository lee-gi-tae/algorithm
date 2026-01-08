def solution(money):
    answer = []
    a = money//5500
    b = money - 5500 * a
    answer = [a, b]
    return answer