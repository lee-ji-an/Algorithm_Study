from itertools import accumulate, chain
import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

# 밑장 빼기 한 번도 안 했을 때 합 / 정훈이 차례에 했을 때 / 상대방 차례에 했을 때
origSum = tuple(accumulate(card for idx, card in enumerate(card) if not (idx % 2)))[-1]
case1 = accumulate((card[i] - card[i-1] for i in range(N-1, 0, -2)), initial=origSum)
case2 = accumulate((card[i-1] - card[i] for i in range(N-2, 1, -2)), initial=origSum)

print(max(chain(case1, case2)))
