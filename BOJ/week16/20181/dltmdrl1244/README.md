## Info
[20181 꿈틀꿈틀 호석 애벌레 - 효율성](https://www.acmicpc.net/problem/20181)

## 💡 풀이 방법 요약
> 투 포인터 풀이
이해를 못함.. 재귀로 풀었는데 왜 안 풀리는지도 모르겠음

```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

'''
먹이를 발견하면 먹을지 말지 선택한다
1) 먹이를 먹는다면 그 뒤로 계속 먹는다. 그리고 처음으로 k를 넘어가는 지점에서 그만두고 에너지를 채운다.
1-1) k를 넘어가는 지점에서 다시 반복.
2) 먹이를 먹지 않고 다음으로 넘어간다.
'''

def start_eat(s):
    if s >= n:
        return 0
    if memo[s] != 0:
        return memo[s]
    
    pos = s
    exp = 0
    while exp < k and pos < n:
        exp += food[pos]
        pos += 1
    
    t1 = (exp - k) + start_eat(pos) 
    t2 = start_eat(s + 1)

    ans = max(t1, t2)
    memo[s] = ans
    return ans


n, k = map(int, input().split())
food = list(map(int, input().split()))
memo = [0] * (n)

print(start_eat(0))
```

## 🙂 마무리
정말어
려워요