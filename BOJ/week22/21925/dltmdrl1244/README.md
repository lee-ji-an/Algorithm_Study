## Info
[21925 짝수 팰린드롬](https://www.acmicpc.net/problem/21925)

## 💡 풀이 방법 요약
> 스택을 이용해서 팰린드롬 여부 판단
- 먼저 스택이 비어있거나 직전에 넣은 값과 다르면 스택에다가 추가해서 팰린드롬을 시작
- 스택이 비어있지 않고 직전에 넣은 값과 같으면, 현재 스택에 있는 값들이 이후에 나오는 값들과 팰린드롬을 이루는지 판별한다
- 만약 이룬다면, 스택을 비우고 인덱스를 끝지점으로 이동시킨다.
- 만약 이루지 않는다면 다음번에 팰린드롬을 또 판별할 수 있도록 스택에 넣는다

n까지 모두 탐색하고 났을 때 스택이 비어있지 않다면, 전체 배열을 쪼개어 팰린드롬을 만들 수 없다는 것을 의미함

## 🙂 마무리
어렵습니다 어려워요