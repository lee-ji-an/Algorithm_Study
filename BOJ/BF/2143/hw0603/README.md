## Info
[2143 두 배열의 합](https://www.acmicpc.net/problem/2143)

## 💡 풀이 방법 요약
`A`와 `B`에 대해 미리 누적 합이 될 수 있는 경우를 모두 구한 다음(전처리), `A`의 누적합들을 순회하면서, T를 만들기 위한 보수가 `B`의 누적합 안에 몇 개 존재하는지를 체크하여 카운터를 증가시켜 주면 된다.  
  
체크 시 `B`를 정렬하고 `bisect` 모듈을 활용하여 이진 탐색 기법을 사용하면 빠르게 풀 수 있다.

## 🙂 마무리
처음부터 각 배열에 대한 누적합을 다 구해두고 풀면 되겠다고 생각을 했었는데, 메모리 제한이 64MB로 다른 문제들보다 빡빡하게 잡혀 있는 편이라 당연히 메모리 초과가 날 줄 알고 시도조차 하지 않았었다.  
한참을 헤매다가 리스트 길이 범위가 최대 1000인 것을 보고 다시 누적합으로 접근했는데 풀렸다-_-; 입력 범위 잘 보자..  
  
처음에 이진탐색으로 정렬된 `B` 안에 `T`에 대한 현재 순회중인 `A` 원소의 보수가 존재하는지만 체크를 해서 카운터를 증가시켜서 틀렸다. 단순히 존재 여부를 확인할 것이 아니라 몇 개가 있는지를 체크해 주어야 한다.

## FYI
-  파이썬에서 단순한 for loop 보다 comprehension expression이 더욱 빠르게 동작한다.
-  누적 합 역시 loop나 comprehension을 통한 반복으로 구하는 것 보다 `itertools.accumulate`가 훨씬 빠르다.
  
따라서, comprehension + `accumulate()`를 같이 사용하면 누적 합 배열을 빠르게 구할 수 있다.
```
@timer(repeat=100, verbose=True)
def case1():
    Asum = []
    s = 0
    for i in range(N):
        for j in range(i, N):
            s += A[j]
            Asum.append(s)

@timer(repeat=100, verbose=True)
def case2():
    # itertools.chain.from_iterable() 로 2차원 iterator들을 평면화
    Asum = [
        item for item in chain.from_iterable(
            accumulate(A[startIdx:N]) for startIdx in range(N)
        )
    ]
```
```
========== <TIMER> ==========
함수명       : case1()
반환값       : 
반복 횟수    : 100 회
평균 호출시간: 32.8110033501 (ms)

========== <TIMER> ==========
함수명       : case2()
반환값       : 
반복 횟수    : 100 회
평균 호출시간: 12.6406224412 (ms)
```
실제로 위와 같이 case2의 구현이 약 3배 더 빠른 것을 확인할 수 있다.  
  
`Bsum`의 경우 정렬이 필요하므로 list comprehension으로 선언하여야 하지만, `Asum`은 단순히 반복만 할 것이므로 generator comprehension으로 선언하면 메모리 사용량을 획기적으로 줄일 수 있다.(Lazy evaluation).  
실제로 해당 조건만 수정하여 제출해 보았는데,  
`(70464KB, 752ms)` -> `(53936KB, 760ms)` 으로 시간 증가 폭에 비해 메모리 사용량이 대폭 줄어든 것을 확인할 수 있었다.

## 다시 읽어보면 좋을 자료들
[Generator를 사용해야 하는 이유](https://valuefactory.tistory.com/668)  
[이터레이터와 제네레이터](https://mingrammer.com/translation-iterators-vs-generators)  
[누적 합 속도 비교 (loop vs accumulate)](https://deok2kim.tistory.com/95)  
[List Comprehension의 속도가 빠른 이유](https://stackoverflow.com/questions/22108488/are-list-comprehensions-and-functional-functions-faster-than-for-loops)
[Python Performance Tips - Loops](https://wiki.python.org/moin/PythonSpeed/PerformanceTips#Loops)  
[List Comprehension과 for loop의 인스트럭션 단위 분석](https://stackoverflow.com/questions/31343643/why-list-comprehension-can-be-faster-than-map-in-python?rq=1)  
> Test one: throwing away the result.  
> Test two: Test two: Keeping the result like normal.
>   
> **Real speeds**  
> Test one: for loop is faster by about one-third  
> Test two: list comprehension is faster by about two-thirds  


![relationships](https://user-images.githubusercontent.com/31981462/212229276-07b8e425-388c-4896-a2c7-e49b012a5c11.png)

