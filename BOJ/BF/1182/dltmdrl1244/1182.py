import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

def recur(i, partsum):
    global ans
    if i == n-1:
        # 끝까지 봤을 때 누적합이 s와 같다면 ans 1 추가
        if partsum == s:
            ans += 1
        return
    
    # 재귀적으로 리스트의 다음 수를 넣는 경우, 넣지 않는 경우를 모두 호출
    recur(i+1, partsum + arr[i+1])
    recur(i+1, partsum)

recur(0, arr[0])
recur(0, 0)

# s가 0일 때는 모두 포함하지 않을 때도 카운트되는데 크기가 양수라고 했으므로 이 경우는 제외해 주어야 함
print(ans if s != 0 else ans - 1)