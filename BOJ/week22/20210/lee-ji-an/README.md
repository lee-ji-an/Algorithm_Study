## Info
[20210 파일 탐색기](https://www.acmicpc.net/problem/20210)

## 💡 풀이 방법 요약
1. 각각의 문자열을 문자, 숫자 를 기준으로 분리
2. compare 함수에서 정렬 기준을 정의
    - 분리한 문자, 숫자들을 순서대로 비교
    - 숫자, 숫자일 때 
      - 크기 비교 -> 같으면 길이 비교
    - 문자, 문자일 때
      - char 우선순위 비교 -> 한 단어가 다른 단어에 포함될 때, 길이를 비교

## 🙂 마무리
