import sys
input = sys.stdin.readline

n = int(input())
my_par = dict()
leaf_node = set()
par_node = set()
maximum = 0

for _ in range(n - 1):
    par, ch, weight = map(int, input().split())
    my_par[ch] = [par, weight]
    par_node.add(par)       # 최하단 노드를 찾기 위해, 부모가 된 노드도 저장함
    leaf_node.add(ch)       # 최하단 노드를 찾기 위함

leaf_node = list(leaf_node - par_node)      # 부모가 된 노드를 모두 삭제함

weight_dict = dict()
for idx, node in enumerate(leaf_node):      # 맨 아래 노드부터 시작함
    weight_dict[node] = 0
    while True:
        # 해당 반복문은 부모로 이동하면서, 맨 아래 노드부터 어떤 부모까지의 거리를 저장함
        par = my_par[node][0]
        weight_dict[par] = my_par[node][1] + weight_dict[node]
        node = par
        if node not in my_par:
            break

    for other_node in leaf_node[idx + 1:]:
        score = 0
        while True:
            # 해당 반복문은 다른 맨 아래 노드부터 어떤 부모까지의 거리를 저장함
            par = my_par[other_node][0]
            score += my_par[other_node][1]
            other_node = par
            if other_node in weight_dict:
                # 만약 while문에서 찾은 부모와 일치하다면 그대로 끝냄
                break

        maximum = max(maximum, score + weight_dict[other_node])
    maximum = max(maximum, weight_dict[1])      # 1까지만 가는게 더 빠를 수도 있음

    weight_dict.clear()

print(maximum)
