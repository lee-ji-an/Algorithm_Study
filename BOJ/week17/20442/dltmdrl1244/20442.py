import sys
input = sys.stdin.readline
'''
ㅋㅋ루ㅋㅋ 문자열은 (앞뒤로 같은 개수의 K) (n개의 R) (앞뒤로 같은 개수의 K) 구조이다.
문자열의 앞, 뒤에서 K를 하나씩 잡고, 그 안의 R 개수를 센다.
K (R개수) K
KK (R개수) KK
KKK (R개수) KKK
이런 식으로 문자열을 모두 구한다. left와 right가 서로 엇갈리면 종료한다.
'''

# count_r : s ~ e 범위에 있는 R 개수 반환
def count_r(s, e):
    if arr[s] == 'R':
        return r_sum[e] - r_sum[s] + 1
    else:
        return r_sum[e] - r_sum[s]

arr = list(input().rstrip())
if not arr:
    print(0)
    exit()

# 구간합을 이용해서 R 개수를 구한다.
r_sum = [0 for _ in range(len(arr))]
r_count = 0
for i in range(len(arr)):
    if arr[i] == 'R':
        r_count += 1

    r_sum[i] = r_count

left, right = 0, len(arr) - 1
# 처음에는 모든 문자열에서 R만 찾아봄
ans = count_r(left, right)
k = 0 # 지금까지 찾은 K의 개수
while left <= right:
    while 0 <= left < len(arr) and arr[left] != 'K':
        left += 1
    
    # 문자열에서 K를 찾지 못해 범위를 벗어나면 바로 break
    if left >= len(arr):
        break
    
    while 0 <= right < len(arr) and arr[right] != 'K':
        right -= 1
    
    # 문자열에서 K를 찾지 못해 범위를 벗어나면 바로 break
    if right < 0:
        break
    
    r = count_r(left + 1, right - 1)
    if not r:
        # 만약 left ~ right 사이에 더이상 R이 없다면 이제 ㅋㅋ루ㅋㅋ 문자열이 없음
        break
    k += 2 # left right를 딱 잡았으므로 k += 2

    t = k + r
    ans = max(ans, t) 

    left += 1
    right -= 1

print(ans)