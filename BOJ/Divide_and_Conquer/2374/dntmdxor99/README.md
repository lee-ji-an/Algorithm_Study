## Info
[2374 - 같은 수로 만들기](https://www.acmicpc.net/problem/2374)

## 💡 풀이 방법 요약

우선 같은 숫자는 같은 그룹이므로, 그냥 숫자 한 개만 넣음  
양 옆의 숫자를 비교하면서, 양 옆 숫자 중에 작은 애한테 맞춤  
근데 양 옆이 모두 나보다 작다? 그러면 그냥 넘어감  
예를 들면 아래와 같이 됨    
- 7 1 3 10 4
- 7 3 10 4
- 7 10 4
- 10 4
- 10

## 🙂 마무리
느낌은 분할정복인 것 같다.  