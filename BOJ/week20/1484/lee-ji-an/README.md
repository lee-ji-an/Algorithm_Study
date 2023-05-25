## Info
[1484 다이어트](https://www.acmicpc.net/problem/1484)

## 💡 풀이 방법 요약
> 투 포인터 사용

end_ptr: 현재 몸무게  
start_ptr: 성원이가 기억하고 있던 몸무게

`end_ptr x end_ptr - start_ptr x start_ptr`
- G 보다 클 때:  ```start_ptr += 1```
- G 보다 작을 때: ```end_ptr += 1```
- G 와 같을 때: 정답 리스트에 추가 ```start_ptr += 1, end_ptr += 1```

## 🙂 마무리
전형적인 투 포인터 문제인 듯!