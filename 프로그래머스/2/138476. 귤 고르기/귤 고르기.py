from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    kind = defaultdict(int)
    for i in tangerine:
        kind[i] += 1
    sorted_kind = sorted(kind.items(), key = lambda x:x[1], reverse = True)
    for key, factor in sorted_kind:
        k -= factor
        answer += 1
        if k <= 0:
            break
    return answer