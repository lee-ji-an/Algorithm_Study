from itertools import combinations
while True:
    arr = list(map(int, input().split()))
    if arr == [0]:
        break
    for combi in combinations(arr[1:], 6):
        print(*combi)
    print()