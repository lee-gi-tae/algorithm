def solution(str1, str2):
    for i in range(len(str1)):
        a = str1[i:i + len(str2)]
        if a == str2:
            answer = 1
            return answer
        else:
            answer = 2
    return answer