## Info
[7453 합이 0인 네 정수](https://www.acmicpc.net/problem/7453)

## 💡 풀이 방법 요약
`defaultdict`를 이용해서 배열 A와 배열 B로 만들 수 있는 모든 합의 경우를 key로 가지고, 해당 값이 등장한 횟수를 value로 가지는 딕셔너리를 구축한다.  
제네레이터를 이용하여 `(C[i] + D[j] for i in range(N) for j in range(N))` 과 같이 C와 D로 만들 수 있는 모든 합들의 제네레이터를 만들어 준 후, 이를 순회하면서 그 값에 부호만 바꾼 값이 딕셔너리의 키에 존재하는지 여부를 체크하고, 만약 존재한다면 해당 키의 값을 `answer`에 누적해 준다.

## 🙂 마무리
풀긴 풀었는데 PyPy로 11348ms.. 투포인터로는 어떻게 푸는가?
