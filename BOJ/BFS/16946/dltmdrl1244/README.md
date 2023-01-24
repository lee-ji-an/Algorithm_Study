# 링크
[링크](https://www.acmicpc.net/problem/16946)

# 풀이 방법 
> Union-Find

코드의 주석 참고

- 벽을 육지, 길을 호수로 생각
- 각각의 0번 칸은 호수이다. 호수들끼리 인접해 있으면 하나로 합친다. 호수에는 고유 id값이 존재한다.
- 육지에 인접해 있는 호수들의 넓이를 더한다. 여러 면과 인접해 있는 호수가 있을 수 있으므로, 중복해서 더하지 않기 위해 호수의 id값을 저장한다.

# 느낀 점
너무 naive하게 풀었다가 시간 초과를 당한 후

알고리즘2 수업시간에 배운 union find를 사용해야겠다는 생각이 들었고 오랜 시간 끙끙거리다가 맞춰서 기분이 매우 좋음