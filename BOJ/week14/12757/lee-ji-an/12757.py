import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

db = []
key_value = dict()


def binary_search(key):
    left = 0
    right = len(db) - 1
    idx = -1
    while left <= right:
        mid = (left + right) // 2
        if db[mid] > key:
            right = mid - 1
        elif db[mid] < key:
            left = mid + 1
        else:
            idx = mid
            break
    return idx, right, left  # right, left : key 가 db 에 없을 때 경계값 두 개를 반환


def process(case, key, value):
    idx, num1, num2 = binary_search(key)

    # case 1 : 추가
    if case == 1:
        db.insert(num2, key)
        key_value[key] = value
        return

    # case 2 : 수정,  case 3 : 조회
    if idx == -1:
        cand_list = []
        if 0 <= num2 < len(db) and db[num2] - key <= K:
            cand_list.append(db[num2])
        if 0 <= num1 < len(db) and key - db[num1] <= K:
            cand_list.append(db[num1])

        # 수정
        if case == 2:
            if len(cand_list) == 1:
                key_value[cand_list[0]] = value
            elif len(cand_list) == 2:
                if abs(cand_list[0] - key) < abs(cand_list[1] - key):
                    key_value[cand_list[0]] = value
                elif abs(cand_list[0] - key) > abs(cand_list[1] - key):
                    key_value[cand_list[1]] = value
        # 조회
        elif case == 3:
            if len(cand_list) == 1:
                print(key_value[cand_list[0]])
            elif len(cand_list) == 2:
                if abs(cand_list[0] - key) < abs(cand_list[1] - key):
                    print(key_value[cand_list[0]])
                elif abs(cand_list[0] - key) > abs(cand_list[1] - key):
                    print(key_value[cand_list[1]])
                else:
                    print("?")
            else:
                print(-1)
    else:
        if case == 2:
            key_value[key] = value
        else:  # case 3
            print(key_value[key])


for i in range(N):
    key, value = map(int, input().split())
    key_value[key] = value
    db.append(key)

db.sort()

for i in range(M):
    input_list = list(map(int, input().split()))
    if input_list[0] == 1:
        process(1, input_list[1], input_list[2])
    elif input_list[0] == 2:
        process(2, input_list[1], input_list[2])
    else:
        process(3, input_list[1], -1)
