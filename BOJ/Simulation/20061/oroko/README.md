## Info
[20061 모노미노도미노 2](https://www.acmicpc.net/problem/20061)

## 💡 풀이 방법 요약
> 순서대로 차근히 하고 두 줄이 동시에 없어지는 경우를 주의하기

1. 놓는다.
   * 0열에서부터 막힐 때까지 간 후에 바로 앞에 블록 놓기
2. 가득 찬 줄을 확인한다.
   1. 가득 찬 줄 수와 시작 줄 찾기
   2. 가득찬 줄이 없으면 그만
   3. 가득찬 줄 수만큼 뒤에서부터 옮기기
   4. 한 줄씩 밀렸으니 0열은 비워주기
   5. 가득차서 지운 줄 수 반환하면 점수 더하기
3. 연한 구역 확인한다.
   1. 0, 1열 중에 몇 개의 줄에 놓여 있는지 찾기
   2. 안놓여 있으면 그만
   3. 뒤에서부터 줄 수만큼 옮기기
   4. 0, 1열 비워주기
4. 반복이 끝나면 점수와 각 보드의 블럭 수 출력하기

## 🙂 마무리
* 행열을 바꿔서 풀었으면 옮길 때 주소만 행주소만 옮기면 돼서 좋았겠지만 너무 헷갈릴 것 같아서 그냥 했다.
