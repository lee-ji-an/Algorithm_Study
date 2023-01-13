from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
ans = 0

sa = [a[i] for i in range(n)]
sa.insert(0, 0)
sb = [b[i] for i in range(m)]
sb.insert(0, 0)
bdic = {} # b의 부분수열들의 합을 저장해 놓을 딕셔너리. bdic[3] = 2 라면 3을 만들 수 있는 부분수열의 경우의 수가 2가지라는 것

# 빠른 부분합 계산을 위해 1~i까지의 합을 미리 s[i]에 저장
for i in range(1, n+1):
    sa[i] += sa[i-1]

for i in range(1, m+1):
    sb[i] += sb[i-1]

# 배열 arr의 인덱스 j부터 i까지의 합을 반환
def partsum(arr, i, j):
    return arr[i] - arr[j-1]

# b 배열에서 가능한 조합을 모두 고려해 모든 부분합을 딕셔너리에 저장
for combib in combinations_with_replacement([j for j in range(m)], 2): # 부분합을 구한 두 인덱스를 중복조합으로 구함
    tailb, headb = combib
    sumb = partsum(sb, headb+1, tailb+1)

    # 딕셔너리 갱신
    if sumb in bdic:
        bdic[sumb] += 1
    else:
        bdic[sumb] = 1

for combia in combinations_with_replacement([i for i in range(n)], 2):
    taila, heada = combia
    suma = partsum(sa, heada+1, taila+1)

    # t가 되기 위해 suma가 부족한 값이 b배열로 만들 수 있는지 딕셔너리 탐색 후, 있으면 그 값만큼 추가
    if t - suma in bdic:
        ans += bdic[t-suma]

print(ans)