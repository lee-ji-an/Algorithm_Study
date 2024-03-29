## Info

[1062 가르침](https://www.acmicpc.net/problem/1062)

<br>

## 💡 풀이 방법 요약

> 단어들에 포함된 모든 글자 중에서 조합으로 K개를 뽑은 후 읽을 수 있는 최대 단어 개수 구하기

1. alphabets:Set에 단어들에 포함된 모든 글자 저장하기
2. 모든 단어들을 비트로 표현하기 (wordsBit)
3. alphabets에서 {a, n, t, i, c}를 포함해서 K개 뽑기
4. 뽑은 글자들을 비트로 표현하고 해당 글자들을 배웠을 때 몇 개의 단어를 읽을 수 있는지 & 연산으로 구하기
5. 읽을 수 있는 단어 수의 최댓값 구하기

###  [ 주의 ]
단어들에 포함된 모든 글자의 개수보다 K가 더 크거나 같은 경우를 주의해야 한다.
예) antatica, K = 7 인 경우 : 답은 1
<br>나는 모든 글자가 다 뽑혔는데 K개를 다 채우지 못해서 읽을 수 있는지 확인하는 로직에 들어가지 않았었다. 그래서 함수를 한번 더 호출해줬다. 아니면 뽑기 전에 K와 모든 글자 개수를 비교해서 뽑을 개수를 맞춰주는 방법도 있겠다.

<br>

## 🙂 느낀 점
메모리 초과가 날까봐 단어들에 포함된 글자 집합과 배운 글자 집합을 저장하고 연산할 때 Set 대신 비트마스크를 사용해봤다.