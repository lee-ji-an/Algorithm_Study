## Info
[2668 숫자 고르기](https://www.acmicpc.net/problem/2668)

## 💡 풀이 방법 요약

그래프 탐색, 순환 찾기

재방문 여부를 통해 순환을 결정

여기서,

> 1. 탐색하는데 이미 순환/비순환이 결정된 노드다 -> 내가 탐색한 노드들은 모두 비순환이다
>
> 2. 기존에 탐색했던 노드를 다시 거꾸로 확인(재귀 스택 빠져나오기)하는데 사이클이 결정돼 있다 -> 사이클의 출발지점 
> 

사이클을 이루는 노드 갯수 출력

## 🙂 마무리

