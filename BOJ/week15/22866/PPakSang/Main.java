package org.example.study.week15.탑보기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;

/**
 * 8
 * 3 7 1 6 3 5 1 7
 *
 * 5 3 2 1 2 3 5 4 3 7
 *
 * 19 10 8 20 10 10 21
 *
 * 19 10
 *
 * 특정 건물 기준 좌우로 더 큰놈
 * dp? 나보다 더 큰놈 찾으면 답이고, 작은놈이라고해서 나보다 더 큰놈이 어디에 있는지 모른다, 안되고
 * 어떤 수를 기준으로 무조건 나는 걔한테 작거나 크다
 *
 * 지금 확인하는 수보다 더 높은 빌딩 나오면 어차피 그 뒤에 애들한테 더 낮은애는 안보임
 *
 * 다음 애가 작으면, 일단 보류
 * 다음 애가 크면, 어차피 그 다음에 오는애는 날 못보니깐 갱신
 *
 *
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] nums = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        Answer[] dist = new Answer[N];

        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < N; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] <= nums[i]) {
                stack.pop();
            }
            // 다음 확인하는 빌딩이 더 작은 케이스
            if (stack.isEmpty()) {
                stack.add(i);
                continue;
            }

            dist[i] = new Answer(stack.size(), stack.peek());
            stack.add(i);
        }

        stack = new Stack<>();
        for (int i = N-1; i >= 0; i--) {
            while (!stack.isEmpty() && nums[stack.peek()] <= nums[i]) {
                stack.pop();
            }
            // 다음 확인하는 빌딩이 더 작은 케이스
            if (stack.isEmpty()) {
                stack.add(i);
                continue;
            }

            if (dist[i] != null) {
                dist[i].num += stack.size();
                if (i - dist[i].idx > stack.peek()-i) {
                    dist[i].idx = stack.peek();
                }
            } else {
                dist[i] = new Answer(stack.size(), stack.peek());
            }

            stack.add(i);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            if (dist[i] == null) {
                sb.append(0);
                sb.append("\n");
                continue;
            }
            sb.append(dist[i].num);
            sb.append(" ");
            sb.append(dist[i].idx+1);
            sb.append("\n");
        }

        System.out.println(sb);
    }

    static class Answer {
        int num;
        int idx;

        Answer(int num, int idx) {
            this.num = num;
            this.idx = idx;
        }
    }
}
