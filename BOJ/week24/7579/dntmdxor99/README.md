## Info
[7579 앱](https://www.acmicpc.net/problem/7579)

## 💡 풀이 방법 요약
> 1d_array DP를 사용 -> 시간 초과  
> 효율적인 DP를 사용 -> 시간 초과
>   
> 효율적인 DP 방법  
> DP[n][m]을 얻기 위해서는, DP[n - 1][m - memory[n]], DP[n - 1][m]만 알고있으면 된다.  
> 따라서 이를 재귀로 역호출하여 필요한 부분만 얻는 것이 효율적인 DP  
> 근데 알고보니까 그냥 문제 접근 자체부터 잘못했음.

## 🙂 마무리
시간 초과.