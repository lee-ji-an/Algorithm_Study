## Info
[16946](https://www.acmicpc.net/problem/16946)

## 💡 풀이 방법 요약

1. 맵을 돌면서 `빈 공간`에 대해서 bfs를 수행
2. 그 공간에 번호를 부여해서 번호를 맵에 표시 (번호는 2부터 차례대로 부여), 공간 번호와 그 공간의 면적을 key value로 딕셔너리에 저장  
   해당 공간 번호에 대해서 면적이 얼마인지 딕셔너리에 저장  
   ex) 11001   -> 11221  
　　00111　　33111  
　　01010　　31415  
　　10101　　16171
3. 맵을 돌면서 `벽` 에 대해서 상하좌우를 탐색
4. 예를 들어 상하좌우에 존재하는 공간 번호를 탐색 -> 공간번호의 면적을 딕셔너리에서 찾아 그 값만큼 수를 증가시킴

## 🙂 마무리

처음에 10으로 나눈 나머지를 출력하라는 것을 못 봐서 틀렸다
문제를 꼼꼼히 읽자 <= 정말 정말 중요