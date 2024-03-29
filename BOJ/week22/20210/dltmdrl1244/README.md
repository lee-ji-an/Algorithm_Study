## Info
[20210 파일 탐색기](https://www.acmicpc.net/problem/20210)

## 💡 풀이 방법 요약
> PQ, 튜플 사용
- 튜플의 대소비교는 각 인덱스 순서대로 이루어지는 성질을 이용
- 숫자는 모든 문자보다 앞에 있으므로, 튜플의 첫번째 인덱스를 1로, 문자는 2로
- 문자는 한 글자씩 떼서 비교, `ord` 아스키 값을 이용해 소문자인지 대문자인지 비교한 후 넣는 값을 달리 해 줌
- 숫자의 경우 숫자의 끝이 어딘지 모르므로 일단 임시 값에다가 저장해 두다가 문자열이 끝나거나 문자가 나타나면 그 때 넣음
- 그리고 같은 값이라면 앞에 0이 적게 붙은 (숫자 문자열의 총 길이가 짧은) 것이 우선, 따라서 t를 더해 주면서 총 length도 함께 저장, 튜플의 3번째 인덱스로 사용해서 짧은 것이 먼저 나올 수 있게
- n 횟수만큼 `heappop` 하면 된다

## 🙂 마무리
pq짱