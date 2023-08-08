## Info
[15684 사다리 조작](https://www.acmicpc.net/problem/15684)

## 💡 풀이 방법 요약
> BF, DFS


## 🙂 마무리
Python3 는 시간초과
```Python
for l in line:
        if l%2: odd+=1
    if odd>3-count: return
```
이게 시간 초과를 피할 수 있는 코드인 것 같은데 아직 이해하지 못했다 ㅜ.ㅜ 