## Info
[2015 수들의 합](https://www.acmicpc.net/problem/2015)

## 💡 풀이 방법 요약

> 부분합 two sum
> 
> 0~i - 0~j = k 일 때 (j~i 까지의 합이 k 인 경우)
> 
> i 를 확인할 때 위 식을 만족시키는 0~j = 0~i - k 가 존재한다면 경우의 수를 증가시킨다.
> 
> 연속된 수의 합이라서 기존 two sum 과 다르게 정렬하는 솔루션은 낼 수 없어서 Map 을 사용

## 🙂 마무리