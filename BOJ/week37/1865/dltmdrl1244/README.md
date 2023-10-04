## Info
- [1865 웜홀](https://www.acmicpc.net/problem/1865)

## 💡 풀이 방법 요약
- 벨만 포드 알고리즘
- 사이클이 없다는 가정 하에 어떤 정점으로 다시 돌아오는 경로는 최대 v+1개의 정점, v개의 간선을 지난다.
- 1개의 간선을 사용할 때, 2개의 간선을 사용할 때 ... v개의 간선을 사용할 때 각각의 시행에서 모든 간선을 체크하여 거리 정보를 갱신
- 그리고 음의 사이클이 있다면 v+1번째 시행에서 거리 정보가 업데이트되게 된다. 이러면 무조건 출발점으로 돌아올 때 비용이 음수일 수 있다.

## 🙂 마무리
출발점에 대한 언급이 없어서 모든 점이 출발점이 될 수 있는데 왜 1번 정점을 출발점으로만 고려해도 되는가
여기에 자세한 설명 링크가 나와 있다. -> [링크](https://www.acmicpc.net/board/view/72995)
근데 이해가 잘 안 된다. 처음에 내가 짠 코드는 코드 2번 같은 형태인데 시간 초과가 발생해서 구글링 했더니 1번처럼 풀었다.

```python
import sys
input = sys.stdin.readline

def BF(start):
    dist = [sys.maxsize for _ in range(n+1)]
    # dist[start] = 0

    for i in range(n):
        for s, e, t in edges:
            if dist[s] != sys.maxsize and dist[e] > dist[s] + t:
                if i == n-1:
                    return True
                dist[e] = dist[s] + t
    
    return False
            
for _ in range(int(input())):
    n, m, w = map(int, input().split())
    edges = []
    
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    
    flag = 0
    for i in range(1, n+1):
        if BF(i):
            flag = 1
            break
    
    print("YES" if flag else "NO")

    # if BF(1):
    #     print("YES")
    # else:
    #     print("NO")    
```