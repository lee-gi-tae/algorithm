n = int(input())
lis = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
# 상, 하, 좌, 우
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
answer = 0

def merge(line):
    new_line = []
    for x in line:
        if x != 0:
            new_line.append(x)

    res = []
    i = 0
    while i < len(new_line):
        if i + 1 < len(new_line) and new_line[i] == new_line[i+1]:
            res.append(new_line[i] * 2)
            i += 2
        else:
            res.append(new_line[i])
            i += 1
    while len(res) < n:
        res.append(0)

    return res

def move(lis, d):
    dy, dx = d
    new_lis = []
    for row in lis:
        new_lis.append(row[:])

    # 옆
    if dy == 0:
        for i in range(n):
            if dx == -1:
                new_lis[i] = merge(new_lis[i])
            else:
                new_lis[i] = merge(new_lis[i][::-1])[::-1]
    # 위 아래
    else:
        for j in range(n):
            col = []
            for i in range(n):
                col.append(new_lis[i][j])

            if dy == -1:
                col = merge(col)
            else:
                col = merge(col[::-1])[::-1]

            for i in range(n):
                new_lis[i][j] = col[i]
    return new_lis

def cal(lis, cnt):
    global answer
    current_max = max(map(max, lis))
    if current_max * (2 ** (5 - cnt)) <= answer:
        return
    answer = max(answer, max(map(max, lis)))
    if cnt == 5:
        return

    for d in direction:
        next_lis = move(lis, d)
        if next_lis != lis:
            cal(next_lis, cnt + 1)



cal(lis, 0)
print(answer)