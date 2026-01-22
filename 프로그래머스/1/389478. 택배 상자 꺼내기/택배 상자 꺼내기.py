import math

def solution(n, w, num):
    package_delivery = [[0] * w for _ in range(math.ceil(n / w))]
    point = 1

    def right(lis, row):
        nonlocal point
        if row >= len(lis):
            return

        for i in range(w):
            if point > n:
                return
            lis[row][i] = point
            if point == n:
                return
            point += 1

        point += 0
        left(lis, row + 1)

    def left(lis, row):
        nonlocal point
        if row >= len(lis):
            return

        for i in range(w - 1, -1, -1):
            if point > n:
                return
            lis[row][i] = point
            if point == n:
                return
            point += 1

        point += 0
        right(lis, row + 1)

    row = 0
    cnt = 0

    right(package_delivery, row)

    for i in range(len(package_delivery)):
        for j in range(w):
            if package_delivery[i][j] == num:
                    a, b = i, j
    
    for c in range(a, len(package_delivery)):
        if package_delivery[c][b] != 0:
            cnt += 1
            

                        
            

    return cnt