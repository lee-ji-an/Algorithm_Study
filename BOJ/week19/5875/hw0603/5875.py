import sys

brackets = sys.stdin.readline().rstrip()
N = len(brackets)


left_bracket, right_bracket = 0, 0  # 각 괄호의 등장 횟수
left_stack, right_stack = [], []
left_list, right_list = [0]*N, [0]*N  # 각 인덱스별로 등장한 누적 괄호 횟수

for idx, b in enumerate(brackets):
    if (b == '('):
        left_bracket += 1
        left_stack.append(idx)
    else:
        right_bracket += 1
        if (left_stack):
            left_stack.pop()  # 왼쪽 괄호가 남아있을 경우, 짝 맞춰서 제거
        else:
            right_stack.append(idx)  # 왼쪽 괄호가 남지 않았을 경우(오타), 그 시점의 인덱스 저장

    # 현재 인덱스에 지금까지 나왔던 각 괄호의 개수 저장
    left_list[idx] = left_bracket
    right_list[idx] = right_bracket

if (left_bracket > right_bracket):  # 왼쪽 괄호가 더 많을 때
    # 왼쪽 괄호의 총 개수 - (짝 다 맞추고 남은 것들 중 가장 최근에 들어온 시점의 왼쪽 괄호 수) + 1
    print(left_bracket - left_list[left_stack[-1]]+1)
elif (right_bracket > left_bracket):  # 오른쪽 괄호가 더 많을 때
    print(right_list[right_stack[0]])  # 오른쪽 괄호가 제일 처음으로 많아졌을 때의 오른쪽 괄호 수
else:
    print(0)
