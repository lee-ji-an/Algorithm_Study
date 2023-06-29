from itertools import accumulate
from collections import Counter
import sys

N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))  # 입력 리스트
S = [0] + list(accumulate(A))  # 누적 합

cnt = Counter(s % M for s in S)  # 누적 합의 나머지의 개수를 세어주는 Counter 인스턴스

print(sum(c*(c-1)//2 for c in cnt.values()))  # 나머지가 같은 애들 끼리 nC2 조합을 더해줌
