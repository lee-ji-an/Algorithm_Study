from itertools import combinations
while len(board := sorted(map(int, input().split()[1:]))) > 6:
    for i in combinations(board, 6):
        print(*i, sep=' ')
    print()