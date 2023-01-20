from collections import deque

a, b, c = map(int, input().split())

# 돌 개수 총합이 3의 배수가 아니면 균등하게 배분할 수 없으므로 바로 0 출력
if sum([a, b, c]) % 3 != 0:
    print(0)
    exit()

# 돌 개수를 비교하기 위한 리스트 인덱스를 미리 구해놓음
idx = [(0, 1), (0, 2), (1, 2)]
q = deque()
q.append([a, b, c])
# 이미 고려했던 조합인지 판별하기 위해 set 사용, set에는 튜플로 삽입
hist = set()
hist.add((a, b, c))

def swap(i, j):
    if i > j:
        return i-j, j+j
    else:
        return i+i, j-i

while q:
    cur = q.popleft()
    if cur[0] == cur[1] == cur[2]:
        print(1)
        exit()

    for i, j in idx:
        if cur[i] != cur[j]:
            # 돌의 개수가 다른 게 있으면 swap
            cur[i], cur[j] = swap(cur[i], cur[j])

            # swap 해봤더니 이미 고려했었던 조합이 나오면 넣지 않음
            if tuple(cur) not in hist:
                hist.add(tuple(cur))
                q.append(cur)

print(0)