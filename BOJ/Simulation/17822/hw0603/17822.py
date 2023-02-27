from collections import deque
import sys

N, M, T = map(int, sys.stdin.readline().split()) # 원판의 개수, 원판에 적힌 정수의 개수, T 번 회전
cylinder = [deque(int(x) for x in sys.stdin.readline().split()) for _ in range(N)]  # 원판들의 리스트
info = [[int(x) for x in sys.stdin.readline().split()] for _ in range(T)]  # x배수, d 방향, k 칸 회전


for tc in range(T):
    x, d, k = info[tc]
    # 회전하기
    result = 0
    for i in range(N):
        result += sum(cylinder[i])
        if ((i+1) % x == 0):
            cylinder[i].rotate(-k if d else k)
    
    # 원판에 남아있는 인접한 숫자들 중 같은 숫자를 찾아서 지움
    if (result):
        victim_list = []
        # 같은 원판 안에서 인접한 경우
        for i in range(N):
            for j in range(M-1):
                if (cylinder[i][j] and cylinder[i][j+1] and cylinder[i][j] == cylinder[i][j+1]):
                    victim_list.append((i, j))
                    victim_list.append((i, j+1))

            if (cylinder[i][0] and cylinder[i][-1] and cylinder[i][0] == cylinder[i][-1]):
                victim_list.append((i, 0))
                victim_list.append((i, M-1))

        # 다른 원판 중 인접한 경우
        for j in range(M):
            for i in range(N-1):
                if (cylinder[i][j] and cylinder[i+1][j] and cylinder[i][j] == cylinder[i+1][j]):
                    victim_list.append((i, j))
                    victim_list.append((i+1, j))

        # 원판 재생성
        victim_list = list(set(victim_list))

        for x, y in victim_list:
            cylinder[x][y] = 0

        # 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1 더함
        if not (victim_list):
            avg_sum = 0
            zero_cnt = 0
            for i in range(N):
                avg_sum += sum(cylinder[i])
                zero_cnt += cylinder[i].count(0)
            avg = avg_sum / (N*M-zero_cnt)

            for i in range(N):
                for j in range(M):
                    if not (cylinder[i][j]):
                        cylinder[i][j] = cylinder[i][j]-1 if cylinder[i][j] > avg else cylinder[i][j]+1
    else:
        break

ans = 0
for i in range(N):
    ans += sum(cylinder[i])


print(ans)
