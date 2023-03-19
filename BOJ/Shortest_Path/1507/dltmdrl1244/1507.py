import sys
input = sys.stdin.readline

n = int(input())
dist = []
edgesum = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    edgesum += sum(tmp)
    dist.append(tmp)
    
# edgesum = 간선의 거리 합
edgesum //= 2

for i in range(n):
    for j in range(i+1, n):
        # i, j를 다이렉트로 연결한 경로와 같은 거리가 i, j가 아닌 다른 점 k를 거쳐 가는 경로 중에 있다면, 다이렉트로 연결한 경로를 삭제해야 한다.
        for k in range(n):
            if k == i or k == j:
                continue
            # 그러한 k 발견. i, j를 잇는 경로를 삭제함. 삭제해준 경로 거리만큼 edgesum을 차감
            if dist[i][k] + dist[k][j] == dist[i][j]:
                edgesum -= dist[i][j]
                break
            
            # 만약 경유지를 거쳐가는 길 중 더 빠른 길이 있다면 '최단 거리가 주어진다' 라는 문제 조건에 위배되므로 불가능
            if dist[i][k] + dist[k][j] < dist[i][j]:
                print(-1)
                exit()

print(edgesum)