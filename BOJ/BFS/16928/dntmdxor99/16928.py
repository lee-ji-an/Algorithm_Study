from collections import deque

n, m = map(int, input().split())

board = [i for i in range(0, 101)]

for _ in range(n + m):
    i, j = map(int, input().split())
    board[i] = j        # 뱀 혹은 사다리의 목적지로 변경함

dq = deque([1 + 0j])
dq_real_list = set()
while dq:
    cur = dq.popleft()
    for i in range(1, 7):       # 주사위
        r = int((cur + i).real)     # 주사위를 굴려 cur + i 칸에 도착함
        if r == 100:        # 만약 100에 도착했다면
            print(int(cur.imag + 1))        # 횟수를 출력함
            exit(0)
        elif r < 100:       # 100보다 작다면
            if r not in dq_real_list:       # 그리고 방문하지 않았다면 (!)
                dq.append(complex(board[r], cur.imag + 1))      # r번째에 해당하는 보드의 값을 추가함
                dq_real_list.add(r)
