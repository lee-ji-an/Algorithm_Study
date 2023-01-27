## Info

[1963](https://www.acmicpc.net/problem/1963)

<br>

## 💡 풀이 방법 요약

> 4자리 소수를 모두 구하고 각 자리 수의 숫자를 하나씩 바꾸면서 bfs 목표 숫자에 도달하면 종료

1. 4자리 소수를 모두 구함 
2. 4자리의 숫자 를 0~9까지 바꿔보고 그 숫자가 탐색한 적이 없는 수이면서 소수이면 q에 집어넣음
3. 목표 숫자에 도달하면 종료
<br>

## 🙂 느낀 점
```
def changer(totalNumber, digit, n):  # totalNumber의 digit 자리 수를 n으로 바꾸겠다
    s = list(str(totalNumber))
    s[digit] = chr(n + ord('0'))
    return int(''.join(s))
```
숫자의 특정 자리만 바꾸고 싶을 때 이렇게 만들면 간단한 것 같다! (강의 영상에 나오는 방법)