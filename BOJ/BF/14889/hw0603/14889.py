from itertools import combinations
import sys

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

players = set(range(1, N+1))
result = sys.maxsize
for start in combinations(range(1, N+1), N//2):
    link = players - set(start)

    # print(start, link)

    # 스타트 팀의 능력치
    stat_start = 0
    for p1, p2 in combinations(start, 2):
        stat_start += S[p1-1][p2-1]
        stat_start += S[p2-1][p1-1]
    
    # 링크 팀의 능력치
    stat_link = 0
    for p1, p2 in combinations(link, 2):
        stat_link += S[p1-1][p2-1]
        stat_link += S[p2-1][p1-1]
    
    min_diff = abs(stat_link - stat_start)
    
    result = result if min_diff > result else min_diff

print(result)
