import sys
input = sys.stdin.readline


def sol():
    n, k = map(int, input().split())
    maps = list(input().strip())
    stack = []
    ansLen = n - k
    
    for i in range(n):
        while stack and stack[-1] < maps[i] and k > 0:
            # 오등큰수와 매우 흡사함
            # while 현재 숫자 들어오는 숫자보다 스택에 있는 숫자가 작으면 팝함
            # 빼는 횟수만큼 k에서 1을 빼야함
            k -= 1
            stack.pop()
        stack.append(maps[i])

    print(''.join(stack[0:ansLen]))     # n이 내림차순이라면 스택에 숫자가 다 들어감 == k가 0이 아님. 따라서 ansLen만큼 프린트함


if __name__ == "__main__":
    sol()
