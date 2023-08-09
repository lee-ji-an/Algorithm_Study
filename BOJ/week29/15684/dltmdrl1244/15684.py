import sys
from itertools import combinations
input = sys.stdin.readline

def check(lines): 
    # i = 세로줄 시작위치
    for i in range(1, n+1):
        # cur = 현재 위치
        cur = i
        # j = 가로줄
        for j in range(h):
            # 가로줄이 연속되는 경우는 없다고 했으므로, 연속된 가로줄(갈림길)을 만나면 바로 return False
            if 1 < cur < n and j * (n-1) + cur - 1 in lines and j * (n-1) + cur in lines:
                return False
            # 왼쪽으로 갈 수 있는지 체크
            elif cur != 1 and j * (n-1) + cur - 1 in lines:
                cur -= 1
            # 오른쪽으로 갈 수 있는지 체크
            elif cur != n and j * (n-1) + cur in lines:
                cur += 1
        
        # 다 내려왔는데 cur != i면 return False
        if cur != i:
            return False
    
    return True


n, m, h = map(int, input().split())
lines = set()

# 초기 가로줄을 먼저 넣어놓음
for _ in range(m):
    y, x = map(int, input().split())
    lines.add((y-1) * (n-1) + x)

# 추가로 뽑을 수 있는 가로줄들의 배열
candidate = []
for i in range(1, (n-1) * h + 1):
    if i not in lines:
        candidate.append(i)

# 3보다 크면 -1 출력하라 했으므로 골라보는 개수는 3까지만
for c in range(4):
    for new_lines in combinations(candidate, c):
        lines_copy = lines.copy()
        lines_copy.update(new_lines)
        # lines_copy = 이번 시행에서 연결된 가로줄들의 집합

        if check(lines_copy):
            print(c)
            exit()
    
print(-1)