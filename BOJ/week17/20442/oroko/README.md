## Info
[20442 - ㅋㅋ루ㅋㅋ](https://www.acmicpc.net/problem/20442)

## 💡 풀이 방법 요약
> R 누적합과 K 기준 투포인터

1. R의 누적합을 구한다.
2. K 기준으로 양 끝에서 투포인터로 탐색한다.
   * leftK와 rightK에 각각 양끝에서부터 왼쪽, 오른쪽의 K 갯수를 누적해서 저장한다.
   * answer는 R만 취했을 때의 값 = R[L-1]로 초기화하고 시작한다.
   1. answer 갱신 : left ~ right 사이의 R값 + min(leftK, rightK) * 2
   2. leftK와 rightK 중 더 작은 것을 안쪽으로 옮긴다.

## 🙂 마무리
좋은 문제 !

