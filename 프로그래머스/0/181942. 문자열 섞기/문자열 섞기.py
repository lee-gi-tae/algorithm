def solution(str1, str2):
    answer = ''
    length = len(str1)
    for i in range(length):
        answer += (str1[i] + str2[i])
    return answer