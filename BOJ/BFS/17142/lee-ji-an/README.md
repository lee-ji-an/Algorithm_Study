## Info
[17142 연구소 3](https://www.acmicpc.net/problem/17142)

## 💡 풀이 방법 요약
1. 바이러스를 놓을 수 있는 공간을 저장  
2. 전체 맵 칸 수에서 바이러스 자리랑 벽의 갯수를 빼서 빈 공간의 갯수를 저장
3. 바이러스를 놓을 자리를 M개 골라 bfs를 탐색
4. 탐색하면서 탐색한 빈칸의 갯수를 세고 미리 저장해놓은 빈 칸의 수와 같아지면 그 때까지의 거리를 return

## 🙂 마무리
연구소 2 때 들었던 방법(미리 자리를 고르고 bfs)으로 짜보았다.
바이러스를 만나면 활성화되는 게 의미가 있나? 싶었는데 큰 의미는 없었고  
`비활성 바이러스만 마지막으로 남았을 때에도 모든 칸에 바이러스가 퍼진 것으로 봐야한다는 것`
이게 핵심 포인트 !