## Info
[3107 - IPv6](https://www.acmicpc.net/problem/3107)

## 💡 풀이 방법 요약
- 문자열을 ':' 기준으로 split 하고 배열에 저장한다
- 만약 `''` 가 있다면 '::' 가 있는 것이므로 비어있는 자릿수만큼 `0000`을 붙여 준다
- 이 때 `::`으로 split하면 공백이 두 개 생기게 되는데 최초 1회만 수행하도록 flag를 사용한다


## 🙂 마무리
구글링하다 발견한 날로 먹는 코드 

```python
import ipaddress
print(ipaddress.IPv6Address(input()).exploded)
```