import sys

string = sys.stdin.readline().strip()
left_k = []  # left_k[i] = i번째 R의 왼쪽에 있는 K의 개수
right_k = []  # right_k[i] = i번째 R의 오른쪽에 있는 K의 개수


cnt = 0
for ch in string:
    if (ch == 'K'):
        cnt += 1
    else:
        left_k.append(cnt)

cnt = 0
for ch in reversed(string):
    if (ch == 'K'):
        cnt += 1
    else:
        right_k.append(cnt)
right_k.reverse()


result = 0
left, right = 0, len(right_k)
while (left < right):
    result = max(result, (right - left) + 2 * min(left_k[left], right_k[right-1]))
    if (left_k[left] < right_k[right-1]):
        left += 1  # 왼쪽 범위가 더 작으면 left 포인터 전진
    else:
        right -= 1  # 반대 경우 right 포인터 감소

print(result)
