import sys
from collections import Counter
input = sys.stdin.readline


def sol():
    n = int(input())
    maps = list(map(int, input().split()))

    count = Counter(maps)
    stack = []
    ans = [-1] * n
    
    for i in range(n):
        while stack and count[maps[stack[-1]]] < count[maps[i]]:        
            # 스택이 채워져 있어야 함. 오른쪽에 오는 애가 나보다 개수가 많아야 함.
            # 만약 아니라면 뒤에 어떤 값이 나의 오등큰수가 될 수 있으므로 스택에 넣음
            ans[stack.pop()] = maps[i]
        stack.append(i)

    print(*ans, sep=' ')


if __name__ == "__main__":
    sol()