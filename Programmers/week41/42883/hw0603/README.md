## Info
[42883 큰 수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/42883)

## 💡 풀이 방법 요약
[BOJ 2812 크게 만들기](https://www.acmicpc.net/problem/2812) 와 동일한 문제  
  
자연수의 특성상, 길이가 길고 앞 자리만 크면 큰 수가 된다.  
따라서, 앞에서부터 탐색하면서 앞자리에 있는 수를 지우고 뒷 자리의 수로 대체했을 때 더 커질 수 있다면 지워야 한다.  
스택을 사용하여 숫자 하나씩 스택에 push 한 뒤 `stack`의 top에 있는 수가 현재의 수 보다 작다면 그 수를 pop 한다.
  
while문 진입 조건에 따라 `K`개의 숫자보다 덜 지워졌을 수 있으므로, 남은 개수 만큼 원래 수(`number`)의 뒷자리를 잘라 자릿수를 맞춰 준다.

## 🙂 마무리
None
