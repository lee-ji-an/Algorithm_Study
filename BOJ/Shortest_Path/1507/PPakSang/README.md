## Info
[1507 - 궁금한 민호](https://www.acmicpc.net/problem/1507)

## 💡 풀이 방법 요약

다른 노드를 경유해서 가는 경로가 직접 가는 경로보다 더 짧으면 직접 가는 경로는 없어도 된다

문제는 x + y(돌아 가는 경로) = z(직접 가는 경로) 일 때 둘 중 어떤 경로를 포함하냐는 건데 (이 부분에서 좀 오래 걸렸다)

z 가 최단 경로라면 x, y 도 최단경로기 때문에 x 와 y 는 추후에 어차피 선택된다. 따라서 직접 가는 경로를 포함하지 않는다

## 🙂 마무리