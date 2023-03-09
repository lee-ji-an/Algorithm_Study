def solution(n, s, a, b, fares):
    import heapq
    adj_list = [[] for _ in range(n + 1)]
    min_dist_table = []

    for e in fares:
        adj_list[e[0]].append((e[2], e[1]))  # (거리, vertex)
        adj_list[e[1]].append((e[2], e[0]))

    destination_list = (s, a, b)
    for destination in destination_list:
        hq = []
        min_dist_list = [float('inf')] * (n + 1)
        heapq.heappush(hq, (0, destination))
        while hq:
            distance, v = heapq.heappop(hq)
            if min_dist_list[v] <= distance:
                continue
            min_dist_list[v] = distance
            for dist, w in adj_list[v]:
                new_cost = min_dist_list[v] + dist
                if new_cost >= min_dist_list[w]:
                    continue
                heapq.heappush(hq, (new_cost, w))
        min_dist_table.append(min_dist_list)

    answer = float('inf')
    for i in range(1, n + 1):
        answer = min(min_dist_table[0][i] + min_dist_table[1][i] + min_dist_table[2][i], answer)

    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))