import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

odd = (cards[::2])
odd_sum = [0] * (n//2 + 1)
even = (cards[1::2])
even_sum = [0] * (n//2 + 1)

o = e = 0
for i in range(1, n//2+1):
    o += odd[i-1]
    e += even[i-1]
    odd_sum[i] = o
    even_sum[i] = e

# 밑장빼기 하는 모든 경우의 수를 탐색

# 밑장빼기 안 했을 때
ans = odd_sum[-1]

# 상대 차례에 밑장을 뺐을 때
for i in range(n//2 - 1):
    ans = max(ans, odd_sum[i+1] + even_sum[n//2-1] - even_sum[i])

# 내 차례에 밑장을 뺐을 때
for i in range(n//2):
    ans = max(ans, odd_sum[i] + even_sum[n//2] - even_sum[i])

print(ans)