from itertools import accumulate, chain
import bisect
import sys

input = sys.stdin.readline
T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# 미리 A와 B의 부분합이 될 수 있는 수들을 모두 구해둠
Asum = (
    item for item in chain.from_iterable(
        accumulate(A[startIdx:N]) for startIdx in range(N)  # Generator expr
    )
)
Bsum = [
    item for item in chain.from_iterable(
        accumulate(B[startIdx:M]) for startIdx in range(M)
    )
]

# Asum을 순회하면서 T에 대한 item_A의 보수가
# Bsum에 몇 개가 존재하는지 구함 -> B를 정렬한 후 이분탐색 사용
# [주의] 단순히 Bsum에 보수가 존재하는지를 판단하는 것이 아니라, 개수를 구해서 더해야 함!
count = 0
Bsum.sort()
for item in Asum:
    complement = T - item
    count += (bisect.bisect_right(Bsum, complement) - bisect.bisect_left(Bsum, complement))
print(count)
