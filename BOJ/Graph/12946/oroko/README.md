## Info

[12946 육각 보드](https://www.acmicpc.net/problem/12946)

<br>

## 💡 풀이 방법 요약

> dfs로 이분 그래프로 색칠하고 색칠했으면 적어도 1, 인접한 수에 따라 2 또는 3 부여하기

1. color 배열 : 0이면 방문x, 1이면 색깔1, 2이면 색깔2로 칠해진 것
2. 색칠해야 하는데 안된 곳을 dfs로 색칠하기

### dfs
1. 이 함수에 들어왔으면 일단 색칠을 해야하기 때문에 답은 최소 1
2. 현재 좌표에 대해서 맞닿아있는 6개의 칸에 대하여
   1. 색칠해야 하는데 안돼있으면 다른 색깔로 색칠 보내기(dfs)
   2. 서로 맞닿아있는 (i,j), (ni,nj)이 둘 다 색칠되어야 하므로 답은 최소 2
   3. (ni,nj)를 색칠하고 왔는데 (i,j)와 같은 색으로 돌아왔으면 색깔 추가해야 하므로 답은 3

<br>

## 🙂 느낀 점
답이 최대 3이고 현재 칸을 둘러싼 6개의 칸과 비교하는 것까지는 갔는데 마무리가 안돼서 결국 강의 시청 ..<br>
세상에 이렇게나 간단하고 깔끔한 로직 근데 이제 내가 짤 수는 없는 ...
