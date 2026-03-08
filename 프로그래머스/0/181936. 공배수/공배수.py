def solution(number, n, m):
    if number % m == 0:
        if number % n == 0:
            if number != 1:
                return 1
    return 0