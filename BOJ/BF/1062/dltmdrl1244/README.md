# 문제 링크
[링크](https://www.acmicpc.net/problem/1062)

# 풀이 방법 요약
> 비트 마스크로 학습한 단어들을 기록

먼저, 단어의 앞에는 항상 `anta` 가 붙고, 뒤에는 `tica` 가 붙기 때문에, 특정 단어를 읽기 위해서는 `a, n, t, i, c` 글자들은 무조건 학습해야 한다. 그말인즉 저 5개 글자를 무조건 학습한다고 가정하고 추가로 학습 여부를 판단할 글자 수는 21개, 그 중 k-5개를 고르는 것이다.

일단 조합을 사용해서 브루트 포스로 `21개 단어 중 k-5개를 선택하는 조합`을 구하고, 각 조합에 대하여 추가적으로 학습한 단어들을 비트 시프트 연산(`<<`) 과 알파벳의 아스키 코드값을 표현하는 `ord` 함수를 이용해서 배운 글자의 정보를 하나의 정수로 나타낸다. (예를 들어 `a, b, c, d`를 학습했을 경우 `0..001111`, 즉 `15`가 된다)

여기서 `a n t i c` 글자들만 학습한 경우에 정수는 `532741` 이 되므로 초기값을 `532741` 로 잡았다.

그리고 학습 정보와 어떤 단어를 `AND` 연산 하면, 단어에 포함된 글자는 1로 비트가 설정되어 있는데 학습 정보의 그 글자의 비트가 0이면 `AND` 했을 때 값이 날아간다.

즉 `AND` 연산을 수행했을 때 `그 단어와 일치하는 정수`가 나오지 않으면 배우지 않은 글자가 포함되어 있어 비트가 0으로 날아가 버렸다는 뜻이므로, `학습한 글자들로 그 단어는 읽을 수 없다`는 결과가 도출된다.

# 느낀 점
비트 마스크를 사용하는 것이 낯설어서 처음에는 단어를 읽을 수 있는지의 여부를 비트 마스크를 사용 안하고 풀어서 단어의 길이만큼의 시간이 추가로 소요되어 시간 초과가 발생하였다.

그래서 비트 마스크를 사용하니 뚝딱 풀렸다.

보수적인 사람이 되지 말도록 하자..

아래는 naive한 방법을 사용했었던 보수적인 나의 코드

```python
import sys
from itertools import combinations
input = sys.stdin.readline

learned = ['a', 'n', 't', 'i', 'c']
rest = list(set([chr(i) for i in range(97, 123)]) - set(learned))
n, k = map(int, input().split())
words = [input()[4:-4] for _ in range(n)]
ans = float('-inf')

if k < 5:
    print(0)
    exit()

def check(chosen):
    cnt = 0
    for word in words:
        flag = 0
        for w in word:
            if w not in chosen:
                flag = 1
        if not flag:
            cnt += 1

    return cnt

def combination(chosen):
    global ans
    if len(chosen) == k:
        ans = max(ans, check(chosen))
        return

    for letter in rest:
        if letter not in learned:
            combination(chosen + [letter])

combination(learned)
print(ans)
```
