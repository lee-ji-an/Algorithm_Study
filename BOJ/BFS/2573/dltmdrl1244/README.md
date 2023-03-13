## Info
[2573 빙산](https://www.acmicpc.net/problem/2573)

## 💡 풀이 방법 요약
> 빙산이 두 조각 이상으로 쪼개질 때까지 혹은 넓이가 0이 될 때까지 반복
- 빙산이 두 조각 이상인지의 판별은 각 회차에서 방문하지 않은 빙산에 대해 `BFS` 수행하였을 때 최초에 `flag = 1` 해 주고, `flag`가 1인 상태로 다시 BFS를 수행하려고 할 때로 판별 가능
- 빙산을 입력 받을 때 전체 넓이를 구하고, `melt` 함수 실행 시에 녹아 없어질 넓이만큼을 빼 주는 식으로 종료조건을 탐색
- `melt` 함수에서는 상하좌우에서 물과 맞닿아 있는 면의 개수를 구해서 빼 준다. 음수가 되면 0으로 세팅


## 🙂 마무리
- 처음에는 빙산 중 가장 높이가 큰 놈을 찾으면 최대 그 숫자만큼만 회차를 수행하면 될 줄 알았는데, 한번에 1씩 깎이는 것도 아닐 뿐더러 만약에 가장 높은 빙산이 내륙에 있으면 엄청 오래 걸릴 수도 있는 것이다. 이 부분을 놓쳐서 자꾸 틀렸다고 나와서 꽤 시간을 잡아먹음...