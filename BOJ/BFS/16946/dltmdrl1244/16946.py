import sys
input = sys.stdin.readline

# 벽을 육지, 길을 호수로 생각
# 각각의 0번 칸은 호수이다. 호수들끼리 인접해 있으면 하나로 합쳐진다. 호수에는 고유 id값이 존재한다.
# 육지에 인접해 있는 호수들의 넓이를 더한다. 여러 면과 인접해 있는 호수가 있을 수 있으므로, 중복해서 더하지 않기 위해 호수의 id값을 저장한다.

n, m = map(int, input().split())
board = []
# weighted union find를 위해 id, size를 저장하는 배열
ids = [i for i in range(n*m)]
size = [1 for i in range(n*m)]
ans = [0 for _ in range(n*m)]
walls = []
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

# 전체 board를 1차원 배열로 만들고 tmp를 이어 붙임
for i in range(n):
    tmp = list(input().rstrip())
    for j in range(m):
        # 벽이라면 나중에 빠른 접근을 위해 따로 벽 배열에 저장해둠
        if tmp[j] == '1':
            walls.append(i * m + j)
    board += tmp

# union-find에 필요한 함수1. 어떤 노드의 root노드를 찾아 반환
def root(a):
    while ids[a] != a:
        a = ids[a]
    return a

# union-find에 필요한 함수2. 어떤 두 노드가 연결되어 있는지(각자가 속한 트리의 root가 같은지) 여부를 반환
def connected(p, q):
    return root(p) == root(q)

# union-find에 필요한 함수3. 어떤 두 노드가 연결되어 있지 않다면 같은 트리로 병합
# 이 때 크기(깊이)가 더 큰 트리의 root 노드 아래에 작은 트리의 root 노드를 붙인다.
# 만약 크기가 같다면 앞의 트리의 root 노드 아래에 작은 트리의 root 노드를 붙인다.
def union(p, q):
    if connected(p, q):
        return

    id1, id2 = root(p), root(q)
    if size[id1] >= size[id2]:
        ids[id2] = id1
        size[id1] += size[id2]
    else:
        ids[id1] = id2
        size[id2] += size[id1]

# 벽이 아닌 칸들에 대해 이웃 노드들을 살펴보면서 합친다
for i in range(n*m):
    if board[i] == '0':
        for j in range(4):
            nxt = (i + m * dy[j] + dx[j])

            # 보드의 행 중 가장 왼쪽 칸이면 왼쪽을 탐색하지 않음
            if i % m == 0 and i != 0 and j == 1:
                continue

            # 보드의 행 중 가장 오른쪽 칸이면 오른쪽을 탐색하지 않음
            if (i+1) % m == 0 and j == 2:
                continue

            # 만약 0인 칸을 발견했고 그 두개가 root가 다르다면 서로 합친다.
            if 0 <= nxt < n*m:
                if board[nxt] == '0' and root(i) != root(nxt):
                    union(i, nxt)

# 각각의 벽들에 대해서 주변에 인접해 있는 벽이 아닌 칸들의 넓이를 더한다.
for i in walls:
    temp = 1
    # 이 때 같은 칸들을 중복해서 더하지 않도록 더한 root를 set에 기록한다.
    v = set()
    for j in range(4):
        nxt = (i + m * dy[j] + dx[j])

        if i % m == 0 and i != 0 and j == 1:
            continue

        if (i+1) % m == 0 and j == 2:
            continue

        # 만약 더하지 않은 호수를 발견하면 더한다.
        if 0 <= nxt < n*m:
            if board[nxt] == '0' and root(nxt) not in v:
                temp += size[root(nxt)]
                v.add(root(nxt))
    ans[i] = temp % 10

# 답 출력
for i in range(n*m):
    print(ans[i], end="")
    if (i + 1) % m == 0:
        print()