import sys

N = int(sys.stdin.readline())

if (N == 1):
    print(0)  # N=1 일때 arr이 비어있으므로 IndexError 처리
    sys.exit()

def prime_list(n):
    data = [True] * (n+1)  # N개 요소에 True 설정(일단 모두 소수로 간주)
    end = int(n ** 0.5)  # n의 최대 약수가 sqrt(n) 이하이므로 sqrt(n)까지 검사

    for num in range(2, end+1):
        if (data[num]): # num이 소수라면
            for j in range(num*2, n+1, num): # num 이후에 등장하는 num의 배수들은 소수가 아님
                data[j] = False
    
    return [i for i in range(2, n+1) if data[i]]

arr = prime_list(N)

# 투 포인터 사용
left, right = 0, 0
subtotal = arr[left]
count = 0

while (right < len(arr)-1):
    # 연속된 부분합이 N과 같으면 카운트 증가
    # arr이 정렬된 배열이므로 left만 옮기면 합이 작아짐.
    # -> right도 같이 한 칸 증가
    if (subtotal == N):
        count += 1
        subtotal -= arr[left]
        left += 1
        right += 1
        subtotal += arr[right]
    # 연속합이 N보다 작다면 더 큰 범위를 봐야 하므로 right 증가
    elif (subtotal < N):
        right += 1
        subtotal += arr[right]
    # 연속합이 N보다 크다면 더 작은 범위를 봐야 하므로 left 증가
    else:
        subtotal -= arr[left]
        left += 1

if (arr[-1] == N):
    count += 1

print(count)
