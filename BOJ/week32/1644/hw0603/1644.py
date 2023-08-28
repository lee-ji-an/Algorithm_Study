import sys

N = int(sys.stdin.readline())

# N == 1인 경우 경우의 수는 0
if (N == 1):
    sys.exit(print(0))

def prime_list(n):
    data = [True] * (n+1)  # 우선 모든 수를 소수로 간주)
    # n의 최대 약수가 sqrt(n) 이하이므로 sqrt(n)까지 검사
    for num in range(2, int(n ** 0.5)+1):
        if (data[num]):  # num이 소수라면
            for j in range(num*2, n+1, num):  # num 이후에 등장하는 num의 배수들은 소수가 아니라고 마킹
                data[j] = False

    return [i for i in range(2, n+1) if data[i]]


arr = prime_list(N)  # 오름차순 정렬된 N이하 소수의 리스트

# 투 포인터
left, right = 0, 0
subtotal = arr[left]
count = 1 if arr[-1] == N else 0  # N이 소수 그 자체인경우 자기 자신도 경우의 수에 포함해야 하므로 카운트가 1부터 시작

while (right < len(arr)-1):
    # 연속된 부분합이 N이면 카운트 증가
    # arr이 정렬된 배열이므로 left만 옮기면 합이 작아짐.
    # -> right도 같이 한 칸 증가
    if (subtotal == N):
        count += 1
        subtotal -= arr[left]
        left += 1
        right += 1
        subtotal += arr[right]
    # 연속합이 N보다 작음 -> 오른쪽 범위를 추가 탐색
    elif (subtotal < N):
        right += 1
        subtotal += arr[right]
    # 연속합이 N보다 큼 -> 왼쪽 범위를 추가 탐색
    else:
        subtotal -= arr[left]
        left += 1

print(count)
