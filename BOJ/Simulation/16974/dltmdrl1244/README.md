## Info

[16974 레벨 햄버거](https://www.acmicpc.net/problem/16974)

<br>

## 💡 풀이 방법 요약
> 찾는 숫자를 구간별로 나누어서 재귀
- 찾는 숫자가 중간에 있으면 앞에 있는 `이전 햄버거의 패티 개수 + 1`
- 찾는 숫자가 중간보다 앞에 있으면 맨 앞의 번 하나를 제외하고 이전 햄버거에서 찾음
- 찾는 숫자가 중간보다 뒤에 있으면 `맨 앞 번 + 중간 패티 + 앞의 이전 햄버거` 만큼을 뺀 숫자를 이전 햄버거에서 찾고 `이전 햄버거의 패티 수 + 1` 만큼을 더함
<br>

## 🙂 느낀 점
재귀는 어렵다