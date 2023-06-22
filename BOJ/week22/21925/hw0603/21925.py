import sys

def isPalindrome(stack, current_pos):
    initial_len = len(stack)
    rev = tuple(reversed(stack))

    for i in range(initial_len):
        if (current_pos + i >= N):
            sys.exit(print(-1))

        # 스택의 top과 현재 위치의 원소 비교
        # 만약 다른 값이라면 팰린드롬이 아님 -> 바로 0 반환
        if (rev[i] != seq[current_pos + i]):
            return 0

    stack.clear()  # 팰린드롬이 성립하면 스택 비우기
    return current_pos + initial_len  # 다음 위치 반환


N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

stack = []
ans, pos = 0, 0

while (pos < N):
    if (stack and (nextPos := isPalindrome(stack, pos))):  # 팰린드롬 성립 하면 pos 업데이트하고 ans 누적
        ans += 1
        pos = nextPos
    else:  # 팰린드롬이 아니라면 스택에 쌓고 한 칸 전진 
        stack.append(seq[pos])
        pos += 1

print(-1 if stack else ans)  # 스택이 비어 있지 않으면 팰린드롬이 성립하지 않은 것
