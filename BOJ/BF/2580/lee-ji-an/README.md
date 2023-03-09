## Info
[2580 스도쿠](https://www.acmicpc.net/problem/2580)

## 💡 풀이 방법 요약
row, col, square(3x3) 마다 set(1 ~ 9까지의 자연수)을 가지고 있고 
숫자를 넣어야하는 곳에 백트랙킹으로 넣었다 뺐다 

모든 칸을 채웠을 때 return 1 을 하고

모든 depth의 함수를 빠져나오게 하기 위해서 다음과 같이 구현
```Python
ret = recur(idx + 1)
if ret:
    return 1
```

## 🙂 마무리

