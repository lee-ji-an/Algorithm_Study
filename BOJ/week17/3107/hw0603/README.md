## Info
[3107 IPv6](https://www.acmicpc.net/problem/3107)

## 💡 풀이 방법 요약
```python
for i in range(8):
    if (len(addr[i]) < 4):  # 4자리가 아니면 앞에 0을 붙여줌
        addr[i] = addr[i].zfill(4)
```
기본적으로 4자리가 아니면 앞에 0으로 채워 준다.  
  
::1 같이 생략된 주소(규칙2)를 처리하기 위해 0그룹들을 복원시켜 준다.
```python
if ('' in addr):
    while (len(addr) > 8):
        addr.pop(addr.index(''))
    while (len(addr) < 8):
        addr.insert(addr.index(''), '0000')
```


## 🙂 마무리
```python
import ipaddress as a;print(a.ip_address(input()).exploded)
```
숏코딩 1등 껄껄
