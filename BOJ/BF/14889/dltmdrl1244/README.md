# 문제 링크
[링크](https://www.acmicpc.net/problem/14889)

# 풀이 방법 요약
> 무식하지만 확실한 브루트 포스

먼저 조합을 사용하여 N명 중 N/2명을 선택하는 경우의 수를 모두 만들고, 선택한 팀의 점수 합, 상대 팀(선택되지 않은 사람들)의 점수 합을 각각 계산, 차의 최솟값을 찾는다.

여기서 1, 2번 선수가 같은 팀이 될 때 `score[0][1]`과 `score[1][0]`을 모두 더해주어야 하는데, 
어차피 둘 다 더할 거니까 미리 `score` 배열 자체를 대각선에 대칭인 위치의 값들을 한 쪽에다가 몰아 주었다. (24~27번 라인)

# 느낀 점
처음에 브루트 포스로 해결하려고 하지 않고 좀 더 기발한 생각을 하느라 머리가 아팠는데... 그냥 몸통박치기 하니까 풀려서 좀 얼떨떨하다.!