## Info
[22866 탑 보기](https://www.acmicpc.net/problem/22866)

## 💡 풀이 방법 요약
> TreeMap과 구현

* 양쪽에서 볼 수 있는 가장 건물 번호를 바로 찾기 위해 TreeMap을 사용해보았다. 
* left{i, j} : i번 건물에서 왼쪽으로 볼 수 있는 건물 수
* right{i, j} : i번 건물에서 오른쪽으로 볼 수 있는 건물 수
* buildings[i] : i번 건물의 번호(i)와 높이
* pq : 높은 건물부터 보기
* cnt[i] : i번 건물에서 볼 수 있는 건물 수 (left.get(i) + right.get(i))
* nearBuilding[i] : i번 건물에서 볼 수 있는 가장 가까운 건물 번호

각 건물 A에 대하여 (26행)
1. 각각 오른쪽과 왼쪽에서 볼 수 있는 가장 가까운 건물 번호 찾기
2. 각 방향에서 가장 가까운 건물(B)이 있다면
   1. val = B에서 해당 방향으로 볼 수 있는 건물 수
   2. B의 높이가 A보다 높다면 B도 볼 수 있으므로 val++
   3. sum += val
   4. 해당 방향 멥에 {A.id, val} 넣기
3. 없으면 해당 방향 맵에 {A.id, 0} 넣기
4. cnt[A.id] = sum
5. nearBuilding[A.id] 결정하기 (헷갈리기 쉬움)

## 🙂 마무리
TreeMap이 바로 생각나서 해봤는데 느린 것 같다.
