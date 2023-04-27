import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

origin_sum = sum(cards[::2])
max_sum = origin_sum

# 밑장을 상대방 에게 줄 때
to_op_sum = origin_sum
for i in range(N-1, -1, -2):
    to_op_sum += (cards[i] - cards[i-1])
    max_sum = max(max_sum, to_op_sum)

# 밑장을 나에게 줄 때
to_me_sum = origin_sum
for i in range(N-3, -1, -2):
    to_me_sum += (cards[i] - cards[i+1])
    max_sum = max(max_sum, to_me_sum)

print(max_sum)