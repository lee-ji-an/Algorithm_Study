## Info
[]()

## 💡 풀이 방법 요약
> 원판 A, B, C 는 각각 'A' 를 빼서 0, 1, 2 인덱스 처리
> 
> 0, 1, 2 갯수 세기
> 
> 각 회차 별로 (막대 상태, 이전에 원판을 끼운 막대 번호, 게임 회차) 정보를 저장
> 
> 막대 번호는 다음 회차에 원판을 옮기지 않을 막대를 고르기 위함
> 
> 각 회차 마다 막대 상태를 확인하고, 정답(0, 1, 2 갯수) 과 동일한 갯수인지 체크
> 
> 같은 상태를 저장하지 않기 위해 막대에 꽂힌 원판 번호열을 Set 에 저장
## 🙂 마무리