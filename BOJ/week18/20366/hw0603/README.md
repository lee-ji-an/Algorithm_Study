## Info
[20366 같이 눈사람 만들래?](https://www.acmicpc.net/problem/20366)

## 💡 풀이 방법 요약
1. 모든 눈덩이들을 2개씩 짝짓는 조합을 구함
2. 구한 조합의 리스트를 두 눈덩이의 합(=눈사람의 키)을 기준으로 오름차순 정렬
   - 정렬된 리스트에서, `i+1`번째 눈사람은 `i`번째 눈사람보다 키가 크면서 가장 키 차이가 적은 눈사람임
3. 나와 나 다음 눈사람을 보며 각 눈덩이가 겹치는 것이 없다면, 현재 최솟값과 비교하여 갱신한다.
4. 루프 탈출 후 최솟값 출력하면 정답

## 🙂 마무리
이 왜 투포인터?  
파이썬 3.10에서 도입된 `itertools.pairwise()`는 때때로 매우 유용하다..!
  
```python
from itertools import combinations as c, pairwise as p
N,s=int(input()),list(map(int,input().split()))
g=lambda x:s[x[0]]+s[x[1]]
print(min(g(a)-g(b)for b,a in p(sorted(c(range(N),2),key=g))if(len(set(b+a))>3)))
```
숏코딩 꿀잼
