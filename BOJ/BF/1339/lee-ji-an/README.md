# 풀이 방법 요약
1. 최댓값을 구해야하므로 숫자를 배정해야할 알파벳이 n개이면 제일 큰 수부터 차례대로 배정할 숫자를 n개 선택
2. 각각의 알파벳에 할당된 값의 비율을 구함
   ex) BAC, CA => A에 할당된 값 = 11, B에 할당된 값 = 100, C에 할당된 값 = 10
3. 할당된 값이 큰 알파벳부터 차례대로 큰 값을 배정

# 느낀점
부등호의 코드를 조금만 변형해서 무식하게 숫자의 값을 배치하는 모든 경우의 수를 검사해서 그 중 가장 큰 값을 구하는 방식으로
코드를 짰지만 역시나 시간초과  
생각보다 알파벳에 할당된 수의 비율을 구하는 게 간단해서 그 점을 이용하면 빠르게 구할 수 있었음