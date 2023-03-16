import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
ans = 0


# lo ~ hi 범위에서 가장 꼭대기 값(여러 개라면 첫 번째) m을 찾아서, m 기준으로 양 옆을 갈라서 재귀
# 재귀에서 리턴 받은 sub array의 최댓값을 m에서 빼 준다. 그리고 최댓값을 리턴
def recur(lo, hi):
    global ans
    
    if lo >= hi:
        return arr[lo]
    
    
    maxval = 0
    for i in range(lo, hi+1):
        maxval = max(maxval, arr[i])
    
    # lo~hi 구역에서의 최댓값의 위치 (여러 개라면 그 중 첫 번째 값)
    idx = arr[lo:hi+1].index(maxval) + lo
    
    
    # idx 왼쪽으로 더 탐색할 영역이 있다면    
    if idx - 1 >= lo:
        a = recur(lo, idx - 1)
        ans += maxval - a
    
    # idx 오른쪽으로 더 탐색할 영역이 있다면
    if idx + 1 <= hi:
        a = recur(idx + 1, hi)
        ans += maxval - a
    
    return maxval
    
recur(0, n-1)
print(ans)