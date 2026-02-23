import heapq

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    pq = []
    heapq.heappush(pq, (0, 1))
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > dist[current_node]:
            continue
        
        for next_node, cost in graph[current_node]:
            new_dist = current_dist + cost
            
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    
    for i in range(1, N+1):
        if dist[i] <= K:
            answer += 1
        
    return answer