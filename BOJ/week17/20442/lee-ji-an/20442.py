import sys
input = sys.stdin.readline

S = input().rstrip()

ans = 0
k_left_cnt = []
k_right_cnt = []

cnt = 0
for i in range(len(S)):  # `R`을 기준으로 왼쪽 k의 갯수
    if S[i] == 'K':
        cnt += 1
    else:
        k_left_cnt.append(cnt)

for i in range(0, len(k_left_cnt)):  # `R`을 기준으로 오른쪽 k의 갯수
    k_right_cnt.append(cnt - k_left_cnt[i])

# two pointer로 pointer 를 옮겨가며 답 구함
left_ptr, right_ptr = 0, len(k_left_cnt) - 1
while left_ptr <= right_ptr:
    ans = max(ans, right_ptr - left_ptr + 1 + min(k_left_cnt[left_ptr], k_right_cnt[right_ptr]) * 2)
    if k_left_cnt[left_ptr] > k_right_cnt[right_ptr]:
        right_ptr -= 1
    else:
        left_ptr += 1
print(ans)
