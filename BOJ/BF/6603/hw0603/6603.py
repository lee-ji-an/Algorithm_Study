from itertools import combinations, starmap
import sys

while ((testCase := list(map(int, sys.stdin.readline().split())))[0]):
    print(*starmap(lambda *x: ' '.join(map(str, x)), combinations(testCase[1:], 6)), sep='\n')
    print()
