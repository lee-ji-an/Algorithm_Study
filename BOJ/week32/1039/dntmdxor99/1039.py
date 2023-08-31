import sys
from collections import deque
input = sys.stdin.readline


if __name__ == "__main__":
    n, k = input().split()
    n = list(n)
    k = int(k)
    l = len(n)

    if l == 1:      # 길이가 1이라면 교환을 못함
        print(-1)
        exit(0)

    ans = '0' * l

    check = set()
    dq = deque()
    dq.append((''.join(n), 0))

    while dq:
        num, cnt = dq.popleft()
        if cnt == k:
            ans = max(ans, num)     # cnt == k라면 대소비교를 해야함 -> 참고로 str도 대소비교 가능
        else:
            num = list(num)
            for i in range(l - 1):
                for j in range(i + 1, l):
                    if i == 0 and num[j] == '0':        # 앞자리 0 방지
                        continue

                    num[i], num[j] = num[j], num[i]     # 교환함

                    temp = ''.join(num)
                    if (temp, cnt + 1) not in check:        # 중복이 아니라면
                        check.add((temp, cnt + 1))
                        dq.append((temp, cnt + 1))

                    num[i], num[j] = num[j], num[i]     # 복구함

    print(-1 if ans == '0' * l else ans)        # 만약 ans를 업데이트하지 않았다면 -1을 출력함