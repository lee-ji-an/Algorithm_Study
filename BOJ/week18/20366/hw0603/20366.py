from itertools import combinations, pairwise
import sys

N = int(sys.stdin.readline())
snowball = list(map(int, sys.stdin.readline().split()))
get_height = lambda x: snowball[x[0]] + snowball[x[1]]
snowman = sorted(combinations(range(N), 2), key=get_height)  # 눈덩이들의 인덱스 조합을 키순으로 오름차순 정렬

result = min(
    (get_height(s2) - get_height(s1))
    for s1, s2 in pairwise(snowman)
    if (len(set(s1 + s2)) == 4)  # s1, s2 눈사람의 각 눈덩이들(인덱스)은 모두 달라야 함
)
print(result)
