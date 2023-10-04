import sys
input = sys.stdin.readline

'''
어떤 지점으로 돌아올 때 음의 사이클이 발생한다면
v-1번을 모두 본 이후에도 비용 갱신이 되어야 한다
만약 v번째 시행에도 시작점으로의 비용이 감소한다면 음의 사이클이 있는 것이다
음의 사이클이 있다면 무조건 YES

없다면 dist[s]가 음수라면 YES
아니라면 NO
'''

def BF(start):
    dist = [sys.maxsize for _ in range(n+1)]
    dist[start] = 0

    for i in range(n+1):
        for s, e, t in edges:
            if dist[e] > dist[s] + t:
                if i == n:
                    return True
                dist[e] = dist[s] + t
    
    return False
            
for _ in range(int(input())):
    n, m, w = map(int, input().split())
    edges = []
    
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    
    # flag = 0
    # for i in range(1, n+1):
    #     if BF(i):
    #         flag = 1
    #         break
    
    # print("YES" if flag else "NO")

    print("YES" if BF(1) else "NO")