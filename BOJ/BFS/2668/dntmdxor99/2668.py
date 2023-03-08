def dfs(start):
    if visited[start]:        # 싸이클이 생김
        ans.add(start)
        return
    else:
        visited[start] = True
        dfs(adj[start])
        visited[start] = False


if __name__ == "__main__":
    n = int(input())
    ori = list(range(1, n + 1))
    lst = [int(input()) for _ in range(n)]
    visited = [False] * (n + 1)
    ans = set()     # 정답 세트
    adj = dict()        # 인접리스트

    for i in range(n):
        adj[i + 1] = lst[i]     # 인접리스트를 만듬

    for i in range(1, n + 1):
        dfs(i)      # 1부터 차레대로 사이클을 찾음

    print(len(ans))
    print(*sorted(list(ans)), sep='\n')
