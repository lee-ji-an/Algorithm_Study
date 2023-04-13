## Info
[14950 정복자](https://www.acmicpc.net/problem/14950)

## 💡 풀이 방법 요약
> Prim 알고리즘

1. Prim으로 모든 도시를 연결하는 최소 weight를 구한다.
2. sum(1 ~ N-2) * t를 더한다.  
   `(weight[v1, v2]+t^0) + (weight[v2, v3]+t^1) + ... + (weight[vN-1, vN]+t^(N-2)) = 모든 weight의 합 + (1+2+...+(N-2))`

## 🙂 마무리
