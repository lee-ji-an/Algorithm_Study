from collections import deque
[n, s, m], board = map(int, input().split()), map(int, input().split())
dp = deque([s])
for i in board:
    check = set()       # 다음 연주 전에는 방문 리스트를 초기화 해야 함
    for _ in range(len(dp)):        # 기존의 dp 길이만큼 반복함
        s = dp.popleft()        # 현재 볼륨을 받아옴
        for j in [s - i, s + i]:        # s - i와 s + i를 반복함
            if 0 <= j <= m and j not in check:      # 볼륨이 범위 안에 있고, 방문하지 않았다면
                dp.append(j)        # dp에 넣음
                check.add(j)        # check에 넣어서 이미 방문한 볼륨을 방지함
print(max(dp) if len(dp) else -1)