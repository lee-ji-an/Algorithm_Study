from collections import defaultdict
import sys

N = int(sys.stdin.readline())
data = defaultdict(int)

for t in range(N):
    T_e, T_x = map(int, sys.stdin.readline().split())
    data[T_e] += 1
    data[T_x] -= 1

current_max, cnt = 0, 0
T_em, T_xm = 0, 0
in_candidate_scope = False
for t in sorted(data.keys()):
    cnt += data[t]  # 현재 시점의 모기 수 구함
    
    # 현재 모기 수가 지금까지 찾은 최댓값보다 크다면 갱신
    if (cnt > current_max):
        current_max = cnt
        T_em = t
        in_candidate_scope = True  # 정답 후보 범위 진입
    
    # 최댓값 갱신 직후 모기 수가 감소하는 시점 마킹
    elif (in_candidate_scope and cnt < current_max):
        T_xm = t
        in_candidate_scope = False  # 정답 후보 범위 탈출

print(current_max)
print(T_em, T_xm)
