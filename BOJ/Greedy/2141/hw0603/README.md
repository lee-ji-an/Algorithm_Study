## Info
[2141 우체국](https://www.acmicpc.net/problem/2141)

## 💡 풀이 방법 요약
가장 최적인 곳에 우체국을 세우려면 우체국을 기준으로 좌 우 마을들 각각의 인구 합이 최대한 동일해야 한다.  
따라서, 마을 정보를 `idx`를 기준으로 정렬하고 인덱스가 낮은 마을부터 탐색하며 인구 정보를 누적해 가다가 누적된 인구가 전체 인구의 절반 이상이 되는 순간의 `idx`가 정답
  
> 마을이 아닌 곳에 우체국을 세울 경우 항상 그 경우와 전체 거리가 동일한 마을 위치에 우체국을 세우는 경우가 존재한다. 따라서 문제 조건에 따라 우체국은 항상 마을 위에만 존재한다.

## 🙂 마무리
처음에는 `idx*p`를 전부 더해서 평균값이 우체국 위치라고 생각하고 풀었는데 틀렸다.  
문제 분류에서 정렬을 보고 마을을 정렬한 다음에 위와 같이 푸니까 통과하기는 하는데.. 첫 풀이가 왜 틀린 것인지 의문