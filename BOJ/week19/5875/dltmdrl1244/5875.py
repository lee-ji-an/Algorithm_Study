import sys
input = sys.stdin.readline

'''
스택이 절대 음수로 내려가면 안 된다
+ -> -는 -2의 효과가 있다. -2를 맞아도 음수가 되면 안 된다. 1 이하일 때마다 갱신해 주고 여기보다는 뒤부터 시작해야한다. last+1 ~ 끝
- -> +는 +2의 효과가 있으므로 음수 -2까지는 커버 가능. 첫 번째로 커버해야 하는 곳을 마크. 0 ~ first
'''

arr = list(input().rstrip())
s = 0
first, last = -1, -1
answer = 0

for i, a in enumerate(arr):
    if a == '(':
        s += 1
    else:
        s -= 1
    
    if s < 2:
        last = i

    if s < 0 and first == -1:
        first = i
    
    if s == -3:
        print(0)
        exit(0)


if s > 0: # ( -> )
    if arr[-1] == '(':
        if len(arr) - 1 >= last:
            print(1)
            exit(0)

    for i in range(last + 1, len(arr)-1):
        if arr[i] == '(':
            answer += 1

else: # ) -> (
    if arr[0] == ')':
        print(1)
        exit(0)

    for i in range(first + 1):
        if arr[i] == ')':
            answer += 1

print(answer)