## Info
[12757 전설의 JBNU](https://www.acmicpc.net/problem/12757)

## 💡 풀이 방법 요약
> TreeMap 사용하기

1. 1이면 map에 넣기
2. 2이면 key 찾고 key가 제대로면 put하기
3. 3이면 key 찾고 조건에 따라 출력하기

### selectKey(...) 
* map에 해당 키가 있으면 키 반환
* minMax와 maxMin 구하기
  * minMax : 입력 키보다 큰 것 중에 가장 작은 존재하는 키
  * maxMin : 입력 키보다 작은 것 중에 가장 큰 존재하는 키
  * 존재하지 않으면 target + K + 1로 설정해서 선택 안되개 하기
* 각각 gap 구하기
* 두 gap 모두 K 초과면 -1 반환
* 둘다 K 이하고 같으면 -2 반환
* 아니면 둘 중 gap이 작은 키 반환

## 🙂 마무리
멋진 TreeMap이구나