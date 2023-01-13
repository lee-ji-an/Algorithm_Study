import sys
from collections import deque
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
q = deque()
dic = {}
mid = n // 2

q.append((0, 0, 0))
while q:
    next_index, depth, partsum = q.popleft()
    # 앞쪽 배열을 모두 탐색했으면 depth는 n//2가 된다. 부분합을 딕셔너리에 저장
    if depth == mid:
        if partsum in dic:
            dic[partsum] += 1
        else:
            dic[partsum] = 1

    # arr[next_index]를 선택하는 경우와 선택하지 않는 경우를 둘 다 q에 삽입하여 모두 고려.
    # 즉 depth가 1씩 증가할 때마다 가지가 2배씩 뻗어나가게 된다
    if depth < mid:
        q.append((next_index + 1, depth + 1, partsum))
        q.append((next_index + 1, depth + 1, partsum + arr[next_index]))

# 뒤쪽 배열 탐색 시작
q.append((mid, mid, 0))
while q:
    next_index, depth, partsum = q.popleft()
    # 뒤쪽 배열까지 탐색 완료, 즉 모든 배열을 탐색했으면 depth가 n이 되며, 이제 딕셔너리를 참조
    if depth == n:
        # 뒤쪽 배열에서 만든 부분합에다가 앞쪽 부분합을 이용해 s로 만들 수 있는지 체크, 있다면 ans에 개수 추가
        if s - partsum in dic:
            ans += dic[s-partsum]

    if next_index <= n-1:
        q.append((next_index + 1, depth + 1, partsum))
        q.append((next_index + 1, depth + 1, partsum + arr[next_index]))

# 만약 s가 0이라면 모두 선택 안해서 합이 0이 되는 경우가 고려된다. 크기가 양수인 부분수열이라 했으므로 제외해줌
if s == 0:
    ans -= 1

print(ans)