import sys
input = sys.stdin.readline

N = int(input())
sequence = list(map(int, input().split()))
stack = [-1] * N
top = -1
ans = 0
idx = 0

# idx 부터 오른쪽에 있는 수들을 살펴봄 -> 팰린드롬인지 확인 후 T/F 반환
def check(idx, top):
    for i in range(top+1):
        if idx + i >= N or stack[top - i] != sequence[idx + i]:
            return False
    return True


while idx < N:
    if top == -1 or (stack[top] != sequence[idx]):
        top += 1
        stack[top] = sequence[idx]
        idx += 1
    else:
        if check(idx, top):  # 팰린드롬인지 확인
            idx = idx + (top + 1)
            top = -1
            ans += 1
        else:  # 팰린드롬이 아니라면 stack 에 넣음
            top += 1
            stack[top] = sequence[idx]
            idx += 1

# 탐색이 끝났을 때 stack이 비워있어야 유효한 경우임
print(ans if ans > 0 and top == -1 else -1)
