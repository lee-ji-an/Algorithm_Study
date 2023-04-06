import sys
import bisect
input = sys.stdin.readline


def find_adj(key):
    idx = bisect.bisect_left(key_list, key)

    if idx == 0:
        # 첫 번째로 들어갈 때
        if abs(key_list[0] - key) <= k:
            return key_list[0]
    elif idx == len(key_list):
        # 마지막으로 들어갈 때
        if abs(key_list[-1] - key) <= k:
            return key_list[-1]
    else:
        # 만약 사이에 낑길 경우
        l_idx, r_idx = key - key_list[idx - 1], key_list[idx] - key
        if l_idx == r_idx and l_idx <= k:
            return -1
        elif l_idx < r_idx and l_idx <= k:
            return key_list[idx - 1]
        elif l_idx > r_idx and r_idx <= k:
            return key_list[idx]

    return -2


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    db = dict()
    key_list = list()
    for _ in range(n):
        key, value = map(int, input().split())
        if key not in db:
            db[key] = value
            bisect.insort(key_list, key)

    for _ in range(m):
        opt = list(map(int, input().split()))

        match opt[0]:
            case 1:
                db[opt[1]] = opt[2]
                bisect.insort(key_list, opt[1])

            case 2:
                if opt[1] in db:
                    db[opt[1]] = opt[2]
                else:
                    index = find_adj(opt[1])
                    if index != -1 and index != -2:
                        db[index] = opt[2]

            case 3:
                if opt[1] in db:
                    print(db[opt[1]])
                else:
                    index = find_adj(opt[1])
                    if index == -1:
                        print('?')
                    elif index == -2:
                        print(-1)
                    else:
                        print(db[index])
