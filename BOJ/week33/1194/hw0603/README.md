## Info
[1194 달이 차오른다, 가자.](https://www.acmicpc.net/problem/1194)

## 💡 풀이 방법 요약
BFS + 비트마스킹으로 풀이한다.  
일반적인 BFS 최단거리 탐색 문제와 기본적으로 동일하지만, 잠겨 있는 문이 있고 먼저 열쇠를 획득한 이후 그 문을 열 수 있는 조건이 추가된 문제이다.  
  
따라서 열쇠를 추가로 획득했을 경우에는 이전에 갔던 경로라도 다시 탐색해 봐야 할 필요가 있다.  
즉, 중복방문 처리를 현재 내가 방문 당시에 획득했던 열쇠를 기준으로 해 주어야 한다.
  
BFS 노드는 `(row, col, keychain)`으로 정의하고, 큐 길이로 잘라서 매 반복 시 마다 `moveCnt`를 증가시켜 준다.  
`keychain`과 `visited`리스트는 비트열로 관리하고, 열쇠 칸이나 문 칸의 값은 `int(f"0x{keyType}", base=16)`을 통해 대소문자 구분 없이 16진수 정수로 변환하여 비트 연산에 사용한다.

1. 탐색할 위치가 열쇠 칸이라면 현재 `keychain`에 열쇠를 추가해야 한다.
```python
keychain = keychain | 1 << 0x0c
```
2. 탐색할 위치가 문 칸이라면 현재 `keychain`으로 문을 열 수 있는지 검증해야 한다.
```python
mask = 1 << 0x0C
isOpened = bool(keychain & mask)
```
3. 탐색할 칸의 중복 방문 여부는 `visited` 리스트의 값과 현재 `keychain`을 `XOR` 연산하여 비트가 다른 위치를 구해 두고, 그 결과를 다시 `visited` 값과 `OR` 연산하여 원래의 `visited` 값과 최종 연산 결과가 달라지는지 확인하여 검증할 수 있다.
```python
hist = visited[row][col]
isDuplicate = (hist == (hist | (hist ^ keychain)))
```
![image](https://github.com/lee-ji-an/Algorithm_Study/assets/31981462/0ab2d2be-dcc3-4877-a806-12f33aa82fa1)


## 🙂 마무리
버스에서 문제 읽고 풀이법을 생각만 해 뒀는데, 집에 와서 그대로 구현했더니 바로 풀려서 기분이 좋았다.  
