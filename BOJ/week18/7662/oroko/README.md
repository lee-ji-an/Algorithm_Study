## Info
[7662 이중 우선순위 큐](https://www.acmicpc.net/problem/7662)

## 💡 풀이 방법 요약
> maxHeap, minHeap, map 사용하기

* `max` : maxHeap pq
* `min` : minHeap pq
* `map` : { 데이터 : 개수 }

1. I이면 max, min에 삽입하고, map에 개수 추가하기
2. D이면
   1. pq가 비었으면 무시
   2. 최댓값 삭제인 경우 max에서 꺼내기
      1. 꺼낸 값이 map에 없으면 버리기 - 최솟값 삭제에서 삭제된 데이터를 의미
      2. 꺼낸 값이 map에 있으면 꺼내고, map에 개수 감소시키기
   3. 최솟값 삭제인 경우 min에서 꺼내기 - 최댓값 삭제와 동일
3. 끝나면 max, min에서 쓰레기값 제거해주고 각각 하나씩 꺼내서 출력하기
4. pq가 비었으면 "EMPTY" 출력

## 🙂 마무리
pq.remove(data)를 사용하면 좋았겠지만 느려서 실패 !