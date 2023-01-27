from collections import deque

n1, n2 = map(int, input().split())
dq, op, check = deque(), ['*', '+'], set()      # 빼기 연산은 필요 없음
if n1 == n2:        # 같다면 끝
    print(0)
    exit(0)
elif n2 == 1:       # n2가 1이라면 나눗셈 하나만 하면 됨
    print('/')
    exit(0)
dq.append([n1, ''])
while dq:
    n, root = dq.popleft()
    for i in range(2):      # 0이면 곱셈, 1이면 덧셈
        nn = n * ((1 - i) * n + i * 2)      # n * n이거나 n + 2인 경우를 분별함
        if nn in check: continue        # 이미 방문한 경우
        if nn < n2:     # nn은 항상 우상향이기 때문에 n2보다 크면 정답이 아님
            dq.append([nn, root + op[i]])
            check.add(nn)
        elif nn == n2:      # 같다면 반환
            print(root + op[i])     # 먼저 root가 더 적고, 더 높은 우선순위를 가지고 있음
            exit(0)
    if 1 in check:      # 1도 방문했는지 확인해야 함 (?)
        continue
    dq.append([1, '/'])      # 1도 탐색해봐야 함
    check.add(1)
else:
    print(-1)
