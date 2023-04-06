## Info
[12757 전설의 JBNU](https://www.acmicpc.net/problem/12757)

## 💡 풀이 방법 요약
초기 db 리스트를 정렬
`명령어 입력시`  
binary search 로 입력 값으로 들어온 key 값의 위치를 찾음 -> key 값을 찾으면 idx 를 반환 없으면 -1을 반환
1. 추가 명령 : binary search 로 찾은 위치에 새로 추가
2. 수정, 조회 명령 :
   -  명령어 의 key 가 없으면 : binary search 에서 입력받은 key 의 경계값 2개를 이용해서 K 범위 안에 있는 key 값을 구함 -> key 값과 후보 값의 차이를 비교해서 답 반환

## 🙂 마무리

