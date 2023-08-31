import sys
from itertools import combinations
input = sys.stdin.readline

# string : 현재 숫자, iter : 남은 교환 횟수
def recur(string, iter):
    global visited, ans
    # 남은 교환횟수가 0이면 정답 비교
    if iter == 0:
        ans = max(ans, int(string))

    else:
        # 방문 처리
        visited.add((string, iter))

        for a, b in combinations([i for i in range(m)], 2):
            # 0은 맨 앞에 올 수 없다는 조건에 대한 예외처리
            if int(string[b]) == 0 and a == 0:
                continue

            # 문자열을 쪼개어 a, b번째 숫자를 교환
            number = string[:]
            number = ''.join([number[:a], number[b], number[a+1:b], number[a], number[b+1:]])

            # 방문하지 않았다면 재귀
            if (number, iter - 1) not in visited:
                recur(number, iter - 1)


n, k = map(int, input().split())
m = len(str(n))
visited = set()
ans = -1
if m == 1:
    print(-1)

else:
    recur(str(n), k)
    print(ans)