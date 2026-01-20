def translate(x):
    x1 = format(x, 'b')
    return x1
    
def cal(a, b):
    cnt_a, cnt_b = 0, 0
    for i in range(len(a)):
        if a[i] == '1':
            cnt_a += 1
    
    for i in range(len(b)):
        if b[i] == '1':
            cnt_b += 1
     
    if cnt_a == cnt_b:
        return True
    else: 
        False

def solution(n):
    answer = n + 1
    while not cal(translate(n), translate(answer)):
        answer += 1

    return answer