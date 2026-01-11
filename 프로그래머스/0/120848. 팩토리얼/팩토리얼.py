def solution(n):
    def cal(answer):
        a = 1
        for i in range(1, answer + 1):
            a *= i
        if a > n:
            return answer - 1
        else:
            answer += 1
            return cal(answer)
    
    return cal(1)