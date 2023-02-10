## Info
[1495 기타리스트](https://www.acmicpc.net/problem/1495)

## 💡 풀이 방법 요약
1. dp 리스트를 모두 False로 초기화  
 ```dp[i][j]``` => i 번째 노래에서 연주가능한 볼륨 j에 대해서 True를 저장하고 불가능한 볼륨은 False를 저장하는 리스트
2. 처음 시작 음악의 볼륨을 True로 변경
3. i 번째 곡에서 연주할 수 있는 볼륨을 True로 변경
   (i-1 번째 리스트에서 True 로 변경돼있는 j에 대해서 (j + volume_range) / (j - volum_range) 한 값을 True로 변경)

> 마지막 곡의 dp 리스트를 끝 값부터 앞으로 탐색 => 최초로 발견된 dp[i][j]이 True 값인 j를 print

## 🙂 마무리
 `이전 곡에서 연주가능한 볼륨을 기록해놓는다` 가 포인트