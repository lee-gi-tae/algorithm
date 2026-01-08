def solution(n):
    answer = 0
    for i in range(n+1):
        if (i % 2) == 1:
            continue
        else:
            answer += i
    return answer