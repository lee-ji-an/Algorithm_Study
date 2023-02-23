from itertools import permutations
from collections import deque
from math import ceil, floor
read = lambda : list(map(int, input().split()))
cal = lambda x, y, z : eval(x + y + z)
n, num, op = *read(), deque(input().split()), read()
ma = -1e+8
mi = 1e+8
num_copy = num.copy()
check = set()
temp = []
for idx, cnt in enumerate(op):
    temp.extend([('+', '-', '*', '/')[idx]] * cnt)      # 변환함
for i in permutations(temp, n - 1):
    if ''.join(i) in check:     # 방문했었다면 패스함
        continue
    check.add(''.join(i))
    for j in i:
        n1 = num.popleft()
        n2 = num.popleft()
        if j == '/':        # 나눗셈이면 음수, 양수에 따라 다르게 해야 함
            if int(n1) < 0:
                num.appendleft(str(ceil(cal(n1, j, n2))))
            else:
                num.appendleft(str(floor(cal(n1, j, n2))))
        else:
            num.appendleft(str(cal(n1, j, n2)))
    ma = max(ma, int(num[0]))
    mi = min(mi, int(num[0]))
    num = num_copy.copy()
print(ma)
print(mi)