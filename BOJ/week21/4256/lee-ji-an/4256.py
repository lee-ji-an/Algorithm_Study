import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    # 내가 stack에 넣었던 수인지 확인하는 리스트
    visited = [False] * (N + 1)
    # 현재 위치까지의 경로를 저장하는 스택 (dfs 탐색할 때 스택을 사용하는 것과 동일한 방식임)
    stack = deque()
    pre_ptr = -1

    # inorder를 순서대로 탐색
    for in_ptr in range(N):
        # 아직 stack 에 넣지 않은 수일 때 -> (in_ptr 이 가리키고 있는 수의 depth가 이전보다 깊어짐) preorder 에서 그 수가 나올 때까지 stack에 넣음
        if not visited[inorder[in_ptr]]:
            while True:
                pre_ptr += 1
                stack.append(preorder[pre_ptr])
                visited[preorder[pre_ptr]] = True

                if preorder[pre_ptr] == inorder[in_ptr]:
                    break
        # 이미 stack 에 넣은 수일 때 -> (in_ptr 이 가리키고 있는 수의 depth가 이전보다 줄어듦) 현재 가리키고 있는 수(a 라고 하겠음)의 왼쪽은 다 탐색을 했다는 의미
        # a가 top이 될 때까지 stack pop (a의 왼쪽만 다 탐색한 것이므로 a는 아직 빼면 안됨)
        else:
            while inorder[in_ptr] != stack[-1]:
                print(stack.pop(), end=' ')

    while stack:
        print(stack.pop(), end=' ')
    print()
