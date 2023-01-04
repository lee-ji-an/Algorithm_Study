## Info
<a href="https://www.acmicpc.net/problem/14225">
    14225 부분수열의 합
</a>

## 💡 풀이 방법 요약
주어진 수열에서 가능한 부분합에 해당하는 index의 원소에 `True`가 저장될 `data`리스트를 하나 선언한다.  
길이가 `N`인 수열 `S`가 주어졌을 때, 이 수열에서 나올 수 있는 부분합의 최댓값은 `sum(S)`이므로, `data`의 길이는 `sum(S)+1` 일 것이다.  
  
`itertools.combinations`를 이용하여 `S`에서 1~N개의 원소를 뽑는 모든 경우를 순회하고, 각 경우마다 합을 구해서 `data[sum]`에 `True`로 마킹해 둔다.  
루프 종료 이후 첫 번째로 `False`가 되는 인덱스를 찾아서 출력하면 정답.

## 🙂 마무리
처음에 1~sum(S) 범위 내의 모든 자연수를 부분합으로 만들 수 있는 경우를 고려하지 않고 `data.index(False)`를 출력하게 하여 `ValueError`가 발생했다.(`data` 리스트 내에 `False` 값이 존재하지 않으므로)  
data 리스트의 길이를 하나 더 늘리거나, `False`가 존재하는지를 미리 검증 후 출력하는 등의 대안이 있었지만, "Ask forgiveness not permission"이라는 파이썬 철학에 따라 `ValueError`만을 예외처리하여 `sum(S)+1`을 출력하도록 구현했다.
