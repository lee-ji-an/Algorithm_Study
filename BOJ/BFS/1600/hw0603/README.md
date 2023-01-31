## Info
[1600 말이 되고픈 원숭이](https://www.acmicpc.net/problem/1600)

## 💡 풀이 방법 요약
`visited` 배열을 해당 좌표에 도달하기 위해 사용한 점프의 개수로 정의하고, `sys.maxsize`로 초기화 해 둔다.  
BFS 노드에 지금까지 경로의 `jump` 횟수를 저장해 두고, `jump`가 `K`보다 작을 때는 일반적인 4방향 노드 탐색 뿐만 아니라 나이트의 이동을 모방한 좌표로의 탐색도 같이 진행해 준다.  
`visited` 배열을 체크할 때는 방문했을 때 jump의 최솟값 업데이트가 가능한 경우에만 방문해야 하므로, 점프를 하는 경우에는 현재 저장된 값보다 `jump+1` 값이 작을 때만 방문해 준다.

## 🙂 마무리
너무 오래 걸려서(5000ms) 다른사람들 코드(2000ms)를 봤는데 크게 다를게 없어 보인다. 어디서 차이가 나는거지??????
  
-> 단순히 전역 scope에서 돌리던 while 문을 `bfs()` 함수 안으로만 넣었더니 2000ms대로 내려갔다..

---
<상세내용 추가>  
[참고링크1: Why does Python code run faster in a function?](https://stackoverflow.com/questions/11241523/why-does-python-code-run-faster-in-a-function)  
[참고링크2: Local variable efficiency](https://wiki.python.org/moin/PythonSpeed/PerformanceTips#Local_Variables)  
  
함수의 로컬 스코프와 전역 스코프의 실행 속도 차이는 전역 변수 참조가 지역 변수 참조보다 더 느린 것에서 기인하며, 실제로 `global` 키워드를 사용하여 함수 내의 변수들을 모두 전역에서 참조하게 할 경우 실행시간이 느려진다.  
  
CPython에서 코드는 인터프리터가 실행할 바이트코드로 컴파일되는데, 함수가 컴파일 될 때 로컬 변수들은 `dict`이 아닌 고정 크기 배열에 저장된다. (함수의 로컬 변수를 동적으로 추가하지 않기 때문에 이러한 구현이 가능함) 이 경우, 로컬 변수를 참조하는 것은 단순히 리스트의 포인터를 참조하고, `PyObject`의 참조 카운트만 증가시키면 된다.  
  
반면, 전역 변수를 참조할 때는 딕셔너리를 통해 참조한다(`LOAD_GLOBAL`). 파이썬에서 딕셔너리를 통해 전역변수를 참조하는 것은 최적화가 잘 되어 있는 편이지만 `dis` 모듈을 통해 바이트코드를 확인해 보면 다음과 같은 차이가 있고, 이름에서 알 수 있듯 `STORE_FAST`의 바이트코드 처리가 훨씬 빠르기 때문에 실행시간이 차이나게 된다.

> 전역변수: `LOAD_GLOBAL`, `STORE_NAME` 사용  
> 지역변수: `LOAD_NAME`, `STORE_FAST` 사용

