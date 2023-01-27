from collections import deque

test_case = int(input())

prime = [False, False] + [True] * 9998
for i in range(2, 10000):
    if prime[i]:
        for j in range(2 * i, 10000, i):
            prime[j] = False        # 에라토스테네스의 체로 소수가 아닌 값을 찾음

prime_ori = prime.copy()        # 복원을 위해 원본을 남김
dq = deque()

for _ in range(test_case):
    dq.clear()      # 이전의 dq 값이 남아있으므로 초기화
    n1, n2 = map(int, input().split())
    if n1 == n2:        # 두 개가 같으면 끝냄
        print(0)
        continue
    else:        
        dq.append([n1, 0])
        while dq:
            num, cnt = dq.popleft()
            prime[num] = False      # 방문했다는 표시
            digit = [(num % i) // (i // 10) for i in [10, 100, 1000, 10000]]        # int 형태로 각 자릿수를 추출함
            if num == n2:       # 탐색에 성공하면 끝냄
                print(cnt)
                prime = prime_ori.copy()
                break
            factor = 1      # 각 자리수에 맞게 곱해야 함
            for i in range(4):
                for j in range(-digit[i] + i // 3, 10 - digit[i]):
                    # 1, 10, 100의 자리의 경우 0도 가능, 1000의 자리는 0을 넣으면 안 됨
                    # 만약 digit[i]가 3이라면 j는 -2, -1, 1, 2, ... , 6
                    if j:
                        new_num = num + factor * j      # 자릿수를 맞춰주고, 기존의 수에 더해줌
                        if prime[new_num]:      # 새로운 숫자가 소수라면
                            dq.append([new_num, cnt + 1])       # 해당 숫자를 큐에 넣음
                            prime[new_num] = False      # 방문했다는 표시

                factor *= 10        # 다음 자릿수로 넘어감
        else:
            print("Impossible")
