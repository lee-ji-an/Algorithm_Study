## Info
[17687 [3차] n진수 게임](https://school.programmers.co.kr/learn/courses/30/lessons/17687)

## 💡 풀이 방법 요약
문제에서 말하는 미리 볼 숫자의 개수 `t`는 `t`까지의 숫자만큼을 조사한다는 것이 아니라, 어떤 수 `X`까지 조사했을 때, 마지막 결과 문자열의 길이를 `t`로 맞추라는 의미이다.  
따라서 `X`의 upper bound를 정의한 뒤, 해당 숫자까지 계산하고 앞에서부터 `t`개의 숫자만 구하여 반환하는 형태로 구현한다.  
  
인원 수가 `m`명이고, 숫자 하나는 최소 한 자리를 차지한다. 따라서 넉넉하게 `0 ~ t*m` 범위를 조사하면 튜브가 외쳐야 하는 숫자들은 항상 `t`개 이상임이 보장된다.  
`X = t*m`으로 가정하고, `n`진법에서 `X`의 자릿수를 계산하면, `l = log_n(t*m)`이 된다.  
  
`itertools.product`를 사용하여 `l`자릿수를 가지는 모든 수를 순회하며 적당히 형식 변환(leading zero 제거, 10~16은 A~E로 변환)하여 배열에 계속 누적해 준다.  
마지막으로 전체 배열의 길이가 `t*m`개를 초과하면 루프를 탈출한 후 `p`번째 플레이어임을 고려하여 순서에 맞는 원소를 차례대로 yield 하는 제네레이터를 정의한 후, `next()`를 활용하여 총 `t`개의 원소를 꺼내며 `answer` 문자열의 뒤에 계속 접합시켜 주면 정답.

## 🙂 마무리
자릿수 맞추는 것과 형식 변환(leading zero 제거 등)하는 데 시간이 꽤 걸렸다. 더 쉽게 푸는 방법이 있을지도..?