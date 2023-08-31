import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N, K = tuple(input().split())
digit = len(N)
N, K = int(N), int(K)
visited = [set() for _ in range(K)]
ans = 0


# pos1 위치, pos2 위치의 수를 바꿔주는 함수
def swap(pos1, pos2, num):
    str_num = str(num)
    num1, num2 = int(str_num[pos1]), int(str_num[pos2])
    if (num1 == 0 and pos2 == 0) or (num2 == 0 and pos1 == 0):  # 맨 앞자리에 0이 오는 것을 방지
        return -1

    return num + (num2 - num1) * pow(10, (digit - pos1 - 1)) + (num1 - num2) * pow(10, (digit - pos2 - 1))


# BFS 수행
q = deque()
q.append(N)
for i in range(K):
    for _ in range(len(q)):
        num = q.popleft()
        # 숫자를 바꿀 자리를 조합으로 생성
        for pos1, pos2 in combinations(range(digit), 2):
            new_num = swap(pos1, pos2, num)
            if new_num == -1 or new_num in visited[i]:
                continue

            # i 번째에 나온 숫자를 visited[i] 에 저장해서 중복 검사 수행
            visited[i].add(new_num)
            q.append(new_num)

if visited[K - 1]:
    print(max(visited[K - 1]))
else:
    print(-1)
