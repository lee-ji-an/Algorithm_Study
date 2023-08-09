import sys
input = sys.stdin.readline

n, c = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

array.sort()
start = 0
end = array[-1] - array[0]
answer = 0

while start <= end:
    mid = (start + end) // 2 # mid 간격으로 공유기를 설치해 본다.
    current = array[0]
    count = 1

    for i in range(1, len(array)):
        if array[i] >= current + mid: # current로부터 떨어진 거리가 mid보다 크거나 같으면 설치할 수 있다.
            count += 1
            # 그 지점에다가 설치하고, current를 옮긴다.
            current = array[i]

    # 다 설치하고 나서 count 개수가 c보다 크거나 같으면, 간격을 더 넓게 설정해도 될 수 있다.
    if count >= c:
        start = mid + 1
        answer = mid
    
    # 공유기 설치 개수가 c보다 작다면, 간격(mid)를 더 작게 설정해야 한다.
    else:
        end = mid - 1

print(answer)