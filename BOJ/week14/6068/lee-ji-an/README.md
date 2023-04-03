## Info
[6068 시간 관리하기](https://www.acmicpc.net/problem/6068)

## 💡 풀이 방법 요약

일 목록 중에서 끝내야하는 시간이 가장 늦는 것부터 탐색

time_ptr 은 새로운 일을 배정할 수 있는 가장 늦은 시간을 가리킴

1. 현재 탐색 과제를 끝내야 하는 시간이 time_ptr보다  더 나중이면
   `time_ptr -= work_size`
2. 현재 time_ptr 보다 빨리 끝내야 할 때
   `time_ptr = end_time - work_size`

## 🙂 마무리

