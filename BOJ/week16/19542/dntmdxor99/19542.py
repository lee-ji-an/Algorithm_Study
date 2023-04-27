import sys
input = sys.stdin.readline


def dfs(node, cnt):
    flag = True
    for i in tree[node]:
        if node == s or i != my_par[node]:
            flag = False
            my_par[i] = node
            cnt += 1
            cnt, d_cnt = dfs(i, cnt)
            if d_cnt > 0:
                return cnt - 1, d_cnt - 1
            else:
                return cnt, 0
    if flag:
        return cnt, d


if __name__ == "__main__":
    n, s, d = map(int, input().split())
    tree = dict()
    my_par = dict()

    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a] = tree.get(a, [])
        tree[a].append(b)
        tree[b] = tree.get(b, [])
        tree[b].append(a)

    cnt = 0
    cnt, _ = dfs(s, cnt)

    print(cnt)