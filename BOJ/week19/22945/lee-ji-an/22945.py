import sys
input = sys.stdin.readline

N = int(input())
ability = list(map(int, input().split()))
ability_idx = []
ans = 0

for i in range(N):
    ability_idx.append((ability[i], i))
ability_idx.sort()

min_ptr = 0
right_ptr = N - 1
left_ptr = 0
# min_ptr : 팀 빌딩에서 능력치의 최솟값을 가리키는 ptr
for min_ptr in range(N):
    # right_ptr : 맨 오른쪽 부터 시작해서 min_ptr이 가리키고 있는 값보다 클 때까지 왼쪽으로 이동하는 ptr
    if ability[right_ptr] < ability_idx[min_ptr][0]:
        while ability[right_ptr] < ability_idx[min_ptr][0]:
            right_ptr -= 1
            if right_ptr < 0:
                break
    # left_ptr : 맨 왼쪽 부터 시작해서 min_ptr이 가리키고 있는 값보다 클 때까지 오른쪽으로 이동하는 ptr
    if ability[left_ptr] < ability_idx[min_ptr][0]:
        while ability[left_ptr] < ability_idx[min_ptr][0]:
            left_ptr += 1
            if left_ptr >= N:
                break
    ans = max(
            ans,
            (right_ptr - ability_idx[min_ptr][1] - 1) * min(ability_idx[min_ptr][0], ability[right_ptr]),
            (ability_idx[min_ptr][1] - left_ptr - 1) * min(ability_idx[min_ptr][0], ability[left_ptr])
        )

print(ans)
