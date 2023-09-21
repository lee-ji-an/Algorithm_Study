import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
due = defaultdict(list)
latest_due = 0 # 가장 늦은 데드라인
ans = 0

for _ in range(n):
    p, d = map(int, input().split())
    # due[d]는 각각이 리스트임
    due[d].append(p)
    latest_due = max(latest_due, d)

for i in range(latest_due + 1):
    if i in due:
        due[i].sort()

# date 부터 latest_due 까지의 idx 중에서 찾음
for date in range(latest_due, 0, -1):
    mP = None
    mIdx = None

    for i in range(date, latest_due + 1):
        if i in due and due[i] and (mP == None or due[i][-1] > mP):
            mIdx = i
            mP = due[i][-1]
    
    # 찾으면 그 일정을 수행, pop
    if mP:
        ans += mP
        due[mIdx].pop()

print(ans)