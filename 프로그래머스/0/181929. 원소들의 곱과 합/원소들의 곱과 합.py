def solution(num_list):
    a = 1
    b = 0
    for i in num_list:
        a *= i
        b += i
    c = b * b
    if c > a:
        answer = 1
    else:
        answer = 0
    return answer