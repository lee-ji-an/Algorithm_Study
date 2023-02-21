## Info
[1182 부분수열의 합](https://www.acmicpc.net/problem/1182)

## 💡 풀이 방법 요약

```Python
dfs(depth, value) 
```
value : 이때까지의 합
depth : 합에 포함할지 /안 할지 고려하는 값의 인덱스

```dfs(depth + 1, value + set_list[depth])```  
➡️입력 리스트 중에서 depth 번째 수를 포함하는 경우

```dfs(depth + 1, value)```  
️️️➡️입력 리스트 중에서 depth 번째 수를 포함하지 않는 경우

## 🙂 마무리

```Python
    if value + set_list[depth] == S:
        cnt += 1
```
새로운 값을 더할 때에만 cnt를 증가시켜야 함 !
