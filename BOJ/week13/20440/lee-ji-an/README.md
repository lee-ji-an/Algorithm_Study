## Info
[20440 🎵니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마🎵 - 1](https://www.acmicpc.net/problem/1234)
`
## 💡 풀이 방법 요약
heapq에 (모기의 번호, 시작 시간), (모기의 번호, 끝 시간) 을 넣음
시간이 작은 것부터 pop해서 검사

1. 해당 모기 번호의 입장시간이라면  
cnt 증가 -> max_cnt 가 갱신되면 start를 갱신, 
2. 해당 모기 번호의 퇴장시간이라면  
cnt 감소 / max_cnt 갱신 flag가 있으면 end를 갱신


## 🙂 마무리
느림 ㅠ
