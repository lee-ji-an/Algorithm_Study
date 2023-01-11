import sys

input = sys.stdin.readline
N, M = map(int, input().split())  # 수열 요소 갯수, 합
A = list(map(int, input().split()))
cnt = 0
start = 0
end = 0
total = A[start]
while(True):
    if total < M:             # total < M 일 때 start를 한 칸 오른쪽으로
        if end == N-1:        # end를 옮기기 전에 end 가 마지막 idx이면 break
            break
        end += 1
        total += A[end]
    elif total > M:             # total > M 일 때 end를 한 칸 오른쪽으로
        total -= A[start]       # start, end 가 같을 때 start +=1 을 해도 맞게 동작
        start += 1
    else:
        cnt += 1             # total == M 일 때 start 와 end를 둘 다 옮김
        if end == N-1:       # end를 옮기기 전에 end 가 마지막 idx이면 break
            break
        total -= A[start]
        start += 1
        end += 1
        total += A[end]

print(cnt)