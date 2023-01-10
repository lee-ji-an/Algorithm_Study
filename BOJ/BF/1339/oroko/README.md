## Info

[1339 단어 수학](https://www.acmicpc.net/problem/1339)

<br>

## 💡 풀이 방법 요약

> 각 알파벳의 가중치 계산해서 높은 순으로 9부터 부여하기 

| 입력                   | 계산(계수가 가중치)                                                                       | 값 대입                              | 출력    |
|----------------------|-----------------------------------------------------------------------------------|-----------------------------------|-------|
| 2 <br> ABCD <br> GGG | 1000A + 100B + 10C + 1D<br>100G + 10G + 1G<br> 계 : 1000A + 111G + 100B + 10C + 1D | {A:9}, {G:8}, {B:7}, {C:6}, {D:5} | 10653 |


1. 해시맵에 {알파벳 : 가중치} 저장
2. 가중치만 정렬해서 9, 8, 7, ... 을 곱해서 더하기

###  Map에서 키 또는 값 배열 추출하기
1. 키 배열 추출하기
    ```java
    Integer[] keys = map.keySet().toArray(new Integer[0]);
    ```
2. 값 배열 추출하기
   ```java
    Integer[] keys = map.values().toArray(new Integer[0]);
   ```
** 특정 타입의 배열로 바로 만들고 싶으면 toArray()의 파라미터에 해당 배열을 꼭 넣어줘야 하고, 아니면 Object 배열로 만들고 각 원소를 캐스팅 해서 쓰는 방법이 있다.

<br>

## 🙂 느낀 점
1. 처음에 순열로 풀어봤는데 시간초과가 나서 다시 풀었다. 나는 왜 자꾸 그리디로 풀게 되지 하면서 알고리즘 분류를 봤는데 그리디였다 !!
2. 원래는 그냥 몇번째 자리인지를 가중치로 하고, 가중치가 같으면 아무 수나 넣어줬는데, 이렇게 하면 한 알파벳이 한 단어 내에 여러번 나올 경우 문제가 생겨서 수를 수 자체로 바라보았다.