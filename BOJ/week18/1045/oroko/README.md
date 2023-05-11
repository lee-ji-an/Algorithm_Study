## Info
[1045 도로](https://www.acmicpc.net/problem/1045)

## 💡 풀이 방법 요약
> Prim 알고리즘

1. 양방향 그래프 만들기  
   i (0~N), j(i+1~N)에 대해서 1부터 순차적으로 weight 부여 
2. 프림 알고리즘으로 MST 만들기
    * 결과적으로 우선순위가 높은 MST가 만들어짐
    * boolean[][] connected에 연결된 엣지 표시(양방향)
    * answer[v]에 v번 노드에 연결된 엣지 수 세기
    * 연결된 노드 수 세기
3. MST를 만들지 못했으면 -1 출력하고 반환
4. M이 총 엣지 갯수보다 작으면 엣지 추가하기
   1. 0번 노드에 연결된 것부터 연결 안됐으면 연결하기
   2. 연결하면서 answer에 엣지 수 증가시키기
   3. M개 연결됐으면 그만
   4. 모든 노드를 봤는데도 M개가 안되면 -1 출력하고 반환
5. answer 배열 출력

## 🙂 마무리
이걸 union-find로 어떻게 푸는걸까?