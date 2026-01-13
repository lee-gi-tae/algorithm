def solution(friends, gifts):
    result = {}
    cal = {friend: 0 for friend in friends}
    degree = {friend: 0 for friend in friends}
    
    for item in gifts:
        give, take = item.split()
        
        if give not in result:
            result[give] = {}
        
        if take not in result[give]:
            result[give][take] = 0
            
        result[give][take] += 1
    
    # 🔹 선물 지수 계산 (최소 수정)
    for give_friend in result:
        for take_friend in result[give_friend]:                
            degree[give_friend] += result[give_friend][take_friend]
            degree[take_friend] -= result[give_friend][take_friend]
        
    # 🔹 비교 (이미 구조 완벽)
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            give_friend = friends[i]
            take_friend = friends[j]

            give_cnt = result.get(give_friend, {}).get(take_friend, 0)
            take_cnt = result.get(take_friend, {}).get(give_friend, 0)
            
            if give_cnt > take_cnt:
                cal[give_friend] += 1
            elif take_cnt > give_cnt:
                cal[take_friend] += 1
            else:
                if degree[give_friend] > degree[take_friend]:
                    cal[give_friend] += 1
                elif degree[take_friend] > degree[give_friend]:
                    cal[take_friend] += 1
                   
    return max(cal.values())
