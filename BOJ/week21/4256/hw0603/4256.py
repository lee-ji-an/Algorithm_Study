import sys
sys.setrecursionlimit(10**8)

def postorder(preorder, inorder):
    if not (preorder):
        return
    if (len(preorder) == 1):
        print(preorder[0], end=' ')
        return
    root = preorder[0]  # 전위순회의 첫 원소는 Root노드
    rootIdx = inorder.index(root)  # 중위순회에서 Root노드의 인덱스
    postorder(preorder[1:rootIdx+1], inorder[:rootIdx])
    postorder(preorder[rootIdx+1:], inorder[rootIdx+1:])
    print(root, end=' ')

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    preorder = list(map(int, sys.stdin.readline().split()))
    inorder = list(map(int, sys.stdin.readline().split()))
    postorder(preorder, inorder)
    print()
