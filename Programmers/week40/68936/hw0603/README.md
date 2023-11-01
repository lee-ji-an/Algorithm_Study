## Info
[68936 쿼드압축 후 개수 세기](https://school.programmers.co.kr/learn/courses/30/lessons/68936)

## 💡 풀이 방법 요약
재귀 + 분할정복으로 풀이한다.  
재귀함수의 인자로 조사 범위를 전달받고, 해당 범위 내에 있는 데이터가 모두 같을 경우에는 그 데이터의 개수를 1로 압축해서 반환한다.  
만약 데이터가 섞여 있다면, 전달받은 범위를 4분할하여 4번 재귀호출하고, 각 호출의 결과를 합산하여 반환하면 된다.

## 🙂 마무리
전달받은 범위 내 데이터가 모두 같은지 판별할 때 순차탐색을 사용했는데, 개선 방법이 있을지 궁금하다.  
처음에 계산결과가 맞지 않아서 삽질을 좀 했었다. 원인을 찾아보니  
```python
    def checkAllSame(a, b, c, d) -> bool:
        lastFound = None
        for i in range(a, c):
            for j in range(b, d):
                if (lastFound and lastFound != arr[i][j]):
                    return False
                lastFound = arr[i][j]
        return True
```
위와 같이 if 조건절에서 `lastFound is not None` 이 맞는 표기이지만, `None`이 아닐 경우에 `True`로 평가된다는 점을 이용하여 `if (lastFound)`와 같이 작성했는데, 만약 `lastFound`에 `정수 0` 이 저장될 경우 이 역시 `False`로 평가되기에 논리에서 오류가 나는 것이였다. `None`과 `0`을 같이 사용할 때는 조심해서 사용해야 하겠다.
