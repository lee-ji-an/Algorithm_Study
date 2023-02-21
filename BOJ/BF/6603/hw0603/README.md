## Info
[6603 로또](https://www.acmicpc.net/problem/6603)

## 💡 풀이 방법 요약
원래 재귀로 구현하는 조합 문제이지만, `itertools.combinations` 모듈로 풀이했다.

## 🙂 마무리
숏코딩을 한 번 해 보고 싶어서 튜플 언패킹과 `map` 함수를 써먹어 보려고 했는데 인자가 6개라 잘 구현되지 않아서 찾아 보다가 `itertools.starmap`이라는 함수를 발견했다.  
  
```python
# 일반적인 map의 경우 단일 인자만 지원
nums = [1, 2, 3, 4]
plus1 = map(lambda x: x+1, nums)  # [2, 3, 4, 5]

# starmap을 사용하면 인자를 여러 개 전달할 수 있음
from itertools import starmap
nums = [(2,5), (3,2), (10,3)]
starmap(pow, [(2,5), (3,2), (10,3)])  # [32, 9, 1000]
```
`itertools` 최고..
