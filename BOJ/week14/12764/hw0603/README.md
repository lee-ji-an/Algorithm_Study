## Info
[12764 싸지방에 간 준하](https://www.acmicpc.net/problem/12764)

## 💡 풀이 방법 요약
기본적인 흐름은 강의실 배정 문제와 같이 `heapq`를 사용하여 풀이한다.  
입력을 받으면서 시작 시간 빠른 순으로 정렬을 해 두고, `heapq` 안에는 종료 시간에 대한 정보를 `push`하면서 각 사용자의 시간을 비교하여 컴퓨터를 이어서 사용할 수 있을 때는 이어서 사용하고, 시간이 겹쳐서 이어서 사용할 수 없을 때는 새로운 컴퓨터를 추가하는 방식을 사용한다.  
  
사용자들이 문제의 조건에 따라 컴퓨터를 사용할 때, 각 컴퓨터 별로 사용된 횟수를 구하기 위해 별도의 `heapq`를 하나 더 사용한다.(사용자들은 idx가 빠른 순으로 사용하기 때문에) 사용 가능한 컴퓨터들의 인덱스 번호를 힙큐에 유지해 두고, 각 컴퓨터가 사용될때는 `pop()`, 사용이 끝난 컴퓨터"들"은 `push()` 해 주면 된다.  
이 때, 사용이 끝난 컴퓨터가 몇 번인지 알아야 하므로 `종료시간`만을 힙큐에 저장했던 강의실 배정 문제와 달리 `(종료시간, 컴퓨터 번호)` 형태의 튜플로 저장해 주어야 한다.  
  
강의실 배정 문제에서는 루프를 모두 순회한 이후 힙큐의 길이가 곧 강의실의 개수가 되었는데, 이번 문제에서는 사용 가능한 컴퓨터 정보를 다시 복구해 주기 위해 힙큐에서 노드를 `pop()`하므로, 단순히 길이로는 필요한 컴퓨터의 개수를 구할 수 없다.  
`comCnt = N - useCnt.count(0)` 형태로 전체 인원 수(=최대 컴퓨터 수) 에서 한 번도 사용되지 않은 컴퓨터들의 개수를 빼 주는 방식으로 구했다.

## 🙂 마무리
처음에 보고 강의실 배정이랑 똑같아서 왜 골드3인가 했는데.. 컴퓨터 별 사용 인원 구하는 게 생각보다 힘들었다.