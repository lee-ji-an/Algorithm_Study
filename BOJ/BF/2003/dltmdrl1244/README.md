# 문제 링크
[링크](https://www.acmicpc.net/problem/2003)

# 풀이 방법 요약
> 부분합 계산에 효과적인 투 포인터 알고리즘

- `s[i]` : 처음부터 `i`까지의 합
- 즉 `i`부터 `j`까지의 부분합은 `s[j] - s[i-1]` 로 표현 가능

두 개의 인덱스를 나타내는 변수인 `head`, `tail`을 사용

자연수의 배열이므로 a부터 b까지의 부분합 A는 b가 더 커질 때 단조 증가함 
- 부분합이 구하고자 하는 `m`보다 크면 `tail`을 줄여 부분합을 줄임
- 부분합이 구하고자 하는 `m`보다 작으면 `head`를 늘려 부분합을 늘림

# 느낀 점
투포인터 알고리즘이 처음에 생각 안나서 같은 것이 있는 조합으로 풀려고 하다가 시간 초과를 당했다. 리스트 순차 접근을 해야 하는 문제는 투포인터를 이용하자

근데 위에 코드는 맞고 아래 코드는 틀린데 뭐가 다른지 아시는분;;??
```python
def partsum(head, tail):
    return s[head] - s[tail - 1]

for head in range(1, n+1):
    while partsum(head, tail) > m and tail < head:
        tail += 1

    if partsum(head, tail) == m:
        ans += 1

print(ans)
```
```python
for head in range(1, n+1):
    partsum = s[head] - s[tail - 1]

    while partsum > m and tail < head:
        partsum -= arr[tail]
        tail += 1

    if partsum == m:
        ans += 1
        
print(ans)
```