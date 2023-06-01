import sys
input = sys.stdin.readline

'''
preorder에서 가장 먼저 나오는 노드가 루트노드이고
inorder에서는 루트노드가 중간에 있다.
루트노드를 inorder에서 찾아서 이 인덱스를 기준으로 왼쪽 sub tree, 오른쪽 sub tree를 정할 수 있다.
그리고 postorder이므로 마지막에 root 노드를 출력한다.
이를 재귀적으로 반복한다.
'''

def postorder(inorder, preorder):
    if not inorder or not preorder:
        return
    
    root = preorder.pop(0)
    root_idx = inorder.index(root)

    postorder(inorder[:root_idx], preorder)
    postorder(inorder[root_idx + 1:], preorder)

    print(root, end=" ")

for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    postorder(inorder, preorder)
    print()