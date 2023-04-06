## Info
[12757 전설의 JBNU](https://www.acmicpc.net/problem/12757)

## 💡 풀이 방법 요약

처음에 키 조회 logN, 삽입 logN 이라고 생각하고 LinekdList 로 키 관리 방법 접근

근데 알고보니 LinkedList 탐색이 O(N), 몬한다

어떻게 logN 으로 잡지 -> 트리 생각했어야 하는듯

모든 키 조회, 삽입/삭제 다 logN 으로 수행하는 자료구조 필요 -> 레드블랙트리(자바 TreeMap)

키를 정렬된 구조로 저장하기 때문에 구간 탐색 할 때도 용이하다

## 🙂 마무리

