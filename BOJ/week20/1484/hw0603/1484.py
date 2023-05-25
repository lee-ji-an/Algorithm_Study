import math
import sys

G = int(sys.stdin.readline())

data = [i for i in range(1, G+1) if not G % i]  # G의 약수들을 구함
# 제곱수라면 제곱근 pop (몸무게는 0이 될 수 없기 때문)
if (math.sqrt(G) == int(math.sqrt(G))):
    data.pop(len(data)//2)


result = []
for i in range(len(data)):
    a, b = data[i], data[-i-1]
    if (a > b):
        break

    cand = (a+b)/2
    if (cand == int(cand)):  # 몸무게가 자연수인경우에만 append
        result.append(int(cand))

if (result):
    print(*reversed(result), sep='\n')
else:
    print(-1)
