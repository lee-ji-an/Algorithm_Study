## Info

[16974 레벨 햄버거](https://www.acmicpc.net/problem/16974)

<br>

## 💡 풀이 방법 요약

> 레벨 L 일 때 N 개 먹을 때의 갯수를 점화식으로 도출
>
> ```java
> if (N == 1) {
>            return L == 0 ? 1 : 0;
>       }
>      else if (2 <= N && N <= 1+num[L-1]) {
>            return bugger(L-1, N-1, num, pNum);
>        }
>        else if (N == 2+num[L-1]) {
>            return pNum[L-1] + 1;
>        }
>        else if (2+num[L-1]+1 <= N && N <= 2+2*num[L-1]) {
>            return pNum[L-1] + 1 + bugger(L-1, N-num[L-1]-2, num, pNum);
>        }
>        else if (N == 3+2*num[L-1]){
>            return pNum[L-1] + 1 + bugger(L-1, N-num[L-1]-3, num, pNum);
>        }
> }
>```

<br>

## 🙂 느낀 점
