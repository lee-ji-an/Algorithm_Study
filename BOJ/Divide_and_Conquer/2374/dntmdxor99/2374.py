import sys
from collections import deque
input = sys.stdin.readline


def sol():
    cnt = 0
    i = 0
    while (n := len(stack)) > 2:
        # 길이가 2와 같거나 작으면 모든 연산이 끝남
        # 1은 당연히 안 되고, 3은 4 1 5 같은 경우에 5에 인덱스가 맞춰져 있으면 잘못된 값을 출력함
        if 0 < i < n - 1:
            m = min(stack[i - 1], stack[i + 1])     # 양 옆에서 작은 애를 고름
            if m >= stack[i]:       # 만약 중간에 값이 더 작다면
                cnt += m - stack[i]
                del stack[i]
                if m == stack[i - 1]:       # 만약 왼쪽 값에 맞춰진다면 i를 한 번 더 빼야함
                    i -= 1
                i -= 1
        elif i == 0:
            if stack[0] < stack[1]:     # 오른쪽 애랑 비교함
                cnt += stack[1] - stack.popleft()
                i -= 1
        elif i == n - 1:        # 왼쪽 애랑 비교함
            if stack[n - 1] < stack[n - 2]:
                cnt += stack[n - 2] - stack.pop()
                i -= 2
        i += 1

    m = max(stack)
    while stack:        # 스택에 남아있다면, 최댓값에서 다 빼면 됨
        cnt += m - stack.pop()

    return cnt


if __name__ == "__main__":
    n = int(input())
    stack = deque()
    stack.append(int(input()))
    for _ in range(n - 1):
        # 어차피 같은 숫자는 하나의 그룹이니까, 숫자 하나만 넣음
        if (temp := int(input())) != stack[-1]:
            stack.append(temp)

    print(sol())
