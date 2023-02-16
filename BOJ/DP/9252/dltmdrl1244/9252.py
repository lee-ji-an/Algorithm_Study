import sys
input = sys.stdin.readline
A = [0] + list(input().rstrip())
B = [0] + list(input().rstrip())
a, b = len(A), len(B)
# LCS[i][j] = A 문자열의 i번째, B 문자열의 j번째 문자를 봤을 때까지의 최대 LCS 길이
LCS = [[-1] * (b) for _ in range(a)]

for i in range(a):
    for j in range(b):
        if i == 0 or j == 0:
            # 좌측, 상단 바운더리
            LCS[i][j] = 0
        
        # 두 문자가 같으면 이전 글자까지의 최대 LCS 길이에서 +1 한 값을 넣어줌 
        if A[i] == B[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        # 두 문자가 다르면 값을 증가시키지 않은 채로 [i][j-1]과 [i-1][j] 중에서 큰 값을 저장
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

# 역추적
i, j = a-1, b-1
res = []
while LCS[i][j] != 0:
    if LCS[i][j-1] == LCS[i][j]:
        j -= 1
    elif LCS[i-1][j] == LCS[i][j]:
        i -= 1
    else:
        res.append(A[i])
        i -= 1
        j -= 1

print(len(res))
if res:
    res.reverse()
    print(*res, sep="")