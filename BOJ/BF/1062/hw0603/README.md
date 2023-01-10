## Info
<a href="https://www.acmicpc.net/problem/1062">
    1062 가르침
</a>

## 💡 풀이 방법 요약
모든 단어가 `anta*tica` 형태이므로 a, c, i, n, t는 기본적으로 배워야 단어를 읽을 수 있다. 따라서 `K`가 5 미만인 경우는 별도로 예외처리를 해 둔다.  
  
`K`가 5 이상이라면 각 단어들에 포함된 문자 정보를 '이진수 형태'로 저장한다.  
이때, '이진수 형태'란 LSB를 `a`에, MSB를 `z`에 대응한 이진수를 말한다. 예를 들어, `a, b, d`를 포함하는 문자열의 경우 `0b0...01011`로 표현된다.  
  
a, c, i, n, t는 기본적으로 학습한다는 가정 하에 로직이 진행되므로, 해당 문자들을 포함한 비트열을 구하여(`532741`) 기본값으로 설정한다.  
`[a-z]`에서 a, c, i, n, t를 제외한 문자들 중 `K-5`개를 뽑는 조합의 경우를 순회하며 뽑힌 문자 조합의 비트열과 기본 비트열(`532741`)을 더해 새로운 비트열을 만들어 주고, 이 새로운 비트열과 각 단어들을 Bit AND 연산했을 때 각 단어가 그대로 나온다면 비트열 안에 각 단어에 포함된 문자 정보가 모두 포함된 것이므로 `cnt`를 증가시킨다.  
  
각 순회 마다 이전의 결과값과 비교하여 최댓값을 유지하고, 루프 종료 후 최댓값을 출력하면 정답.

## 🙂 마무리
처음에는 아래 코드와 같이 각각의 단어에 대해 중복 문자를 제거한 후, 출현하는 빈도에 따라 빈도가 가장 높은 문자들을 우선적으로 학습하면 될 것으로 예상했으나 로직에 문제가 있었다.

```
import sys

N, K = map(int, sys.stdin.readline().split(' '))
words = [set(sys.stdin.readline().rstrip()) for _ in range(N)]  # 글자 중복을 제거한 단어 리스트
alphabets = {chr(97+i): 0 for i in range(26)}  # 각 글자들의 빈도
teach = {}  # 가르칠 글자


# 각 단어를 순회하며 글자의 빈도 구함
for word in words:
    for a in word:
        alphabets[a] += 1

# 출몰 빈도가 높은 K개의 글자에 대하여 teach 딕셔너리에 저장
popular = list(alphabets.items())
popular.sort(key=lambda item: item[1], reverse=True)
for _ in range(K):
    teach[popular.pop(0)[0]] = True

# 각 단어를 다시 순회하며 teach 딕셔너리에 존재하는 글자만으로 읽을 수 있는 단어의 개수 구함
cnt = 0
for word in words:
    cnt = cnt + 1 if all(teach.get(a) for a in word) else cnt
print(cnt)
```

반례
```
3 6
antabcxxxxtica
antabcyyyytica
antaztica

위 경우, z만 추가로 학습하면 한 단어를 읽을 수 있지만 z보다 b의 빈도가 높아 b를 학습하게 되어 읽을 수 있는 단어가 0으로 출력됨

정답: 1
오답: 0
```