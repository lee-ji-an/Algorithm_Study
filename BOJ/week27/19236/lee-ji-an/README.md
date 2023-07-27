## Info
- [19236 청소년 상어](https://www.acmicpc.net/problem/19236)

## 💡 풀이 방법 요약
> BF, 구현 문제

공간의 크기가 4x4로 고정 -> dfs를 이용해서 BF 모든 경우를 탐색

board -> 공간 정보 저장  
fish_info -> 물고기 정보 저장  

dfs 함수에서 매개변수로 board, fish_info를 전달하는데 이를 복사해서 사용해야 함!


## 🙂 마무리
dictionary 복사하는 법을 잘못 써서 디버깅 지옥에 빠졌었다.
주의하도록 하자 ^^
```Python
{key: value[:] for key, value in dict.items()}
```