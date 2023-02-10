import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = {0: 0}
for i in range(n):
    cur_w, cur_v = map(int, input().split())
    tmp = {}
    # 딕셔너리를 순회하면서 새로 들어온 아이템의 무게를 넣을 수 있는 경우를 살핌
    for w, v in bag.items():
        # 이 아이템을 넣어도 무게가 초과하지 않고, 이 아이템을 넣는 것이 기존에 없는 무게일 때, 또는 기존 경우보다 가치가 더 높을 때
        if w + cur_w <= k and (cur_v + v >= bag.get(w + cur_w, 0)):
            tmp[cur_w + w] = cur_v + v

    bag.update(tmp)

print(max(bag.values()))