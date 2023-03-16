## Info
[2374 - 같은 수로 만들기](https://www.acmicpc.net/problem/2374)

## 💡 풀이 방법 요약

divide-n-conquer 를 사용  

- 숫자의 리스트에서 제일 큰 값을 기준으로 왼쪽, 오른쪽으로 divide 함  
  - 왜냐하면, 최종적으로 결과는 리스트에서 제일 큰 값과 모두 같아질 수밖에 없음  
- 따라서, divide 한 리스트 안에서 다시 제일 큰 값을 기준으로 왼쪽 오른쪽으로 나누는 방식  

```python
    left = recur(max_value, start, max_idx - 1)
    right = recur(max_value, max_idx + 1, end)
```
이 코드에서
left 변수: 최댓값을 기준으로 왼쪽 부분에서 최댓값과 같아지기 위해 1을 더한 횟수를 return 받음
right 변수: 최댓값을 기준으로 오른쪽 부분에서 최댓값과 같아지기 위해 1을 더한 횟수를 return 받음



## 🙂 마무리
