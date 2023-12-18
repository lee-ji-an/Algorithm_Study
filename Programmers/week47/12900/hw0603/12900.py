from functools import lru_cache
import sys
sys.setrecursionlimit(10**8)
C = 1_000_000_007

@lru_cache
def fibo(n):
    return 1 if n in {1, 2} else (fibo(n-1) + fibo(n-2)) % C

def solution(n):
    return fibo(n+1)
