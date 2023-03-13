## Info
[2668 숫자 고르기](https://www.acmicpc.net/problem/2668)

## 💡 풀이 방법 요약
그래프를 정의할 때, 문제에서 주어진 input에서 1행에 해당하는 데이터들이 같은 열의 0행을 가리키고 있다고 생각하고 그래프를 정의하면 다음과 같다.  
|1|2|3|4|5|6|7|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|3|1|1|5|5|4|6
```
arr[1]: [2, 3]
arr[2]: []
arr[3]: [1]
arr[4]: [6]
arr[5]: [4, 5]
arr[6]: [7]
arr[7]: []
```
해당 그래프에서는 `arr[i]`의 원소는 i번째 노드와 이어져 있다는 의미이므로 노드 번호를 참조하여 순차적으로 탐색할 수 있다.  
문제의 조건과 같이 첫째 줄에서 뽑은 숫자들의 집합들이 둘째 줄의 숫자 집합과 같으려면, 다음과 같이 노드들이 사이클을 이루고, 그 사이클을 이루는 노드들을 선택하면 된다.
```
1 -> 2 (사이클 형성 X)
1 -> 3 -> 1 -> 3 -> .... -> 1 -> 3 (사이클 형성)

5 -> 4 -> 6 -> 7 (사이클 형성 X)
5 -> 5 -> 5 -> 5 -> .... -> 5 -> 5 (사이클 형성)
```
노드들의 탐색은 DFS를 이용하여 탐색하고, 각 DFS 깊이에서 지금까지 왔던 경로들을 유지하고 있으면 새로 들어온 노드가 이미 경로상에 존재하는 노드인지 파악하여 사이클을 형성하는지 여부를 확인할 수 있다. (지금까지의 경로에 있는 노드가 다시 들어오면 사이클이 형성되는 것)
  
`dfs()` 함수 안에서 경로를 저장하기 위해 사용하는 `pathset` 이외에, 전역 `visited` 배열을 별도로 두어 이미 탐색한 노드에 대한 불필요한 dfs 탐색을 방지할 수 있다.

## 🙂 마무리
