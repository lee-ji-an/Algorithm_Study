## Info
[14391 종이조각](https://www.acmicpc.net/problem/14391)

## 💡 풀이 방법 요약
> 부르트포스, 비트마스킹

각 칸마다 1. 가로로 갈지, 2. 세로로 갈지 두 가지 경우의 수가 있다  
-> 이것을 비트마스킹으로 나타냄 ex) 0100 = 1, 3, 4번칸 `세로` / 2번칸 `가로`

1. 가로 방향 조각 계산
    - 가로 방향으로 전체 칸을 탐색
    - 가로 방향 칸이 나오면 x 10하고 현재 위치의 수를 더함, 세로 방향이 나오면 최종 total 값에 더함 
       (이때까지 더해 온 가로 방향 조각이 끝났으므로)
2. 세로 방향 조각 계산
    - 1번과 반대로 하면됨 

## 🙂 마무리
정답 봤는데 안 봤으면 스터디 전까지 이 생각 못했을 것 같다.
