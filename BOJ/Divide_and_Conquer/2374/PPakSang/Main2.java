package org.example.study.greedy.같은수로만들기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Main2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        // 4 2 10
        Stack<Integer> stack = new Stack<>();
        long answer = 0;

        for (int i = 0; i < n; i++) {
            int cur = Integer.parseInt(br.readLine());
            if (stack.isEmpty()) {
                stack.push(cur);
            }

            int prev = stack.peek();
            if (cur >= prev) {
                answer += cur - stack.pop();
            }
            while (!stack.isEmpty()) {
                prev = stack.peek();
                if (cur >= prev) {
                    stack.pop();
                } else {
                    break;
                }
            }
            stack.push(cur);
        }

        if (stack.size() > 1) {
            int low = stack.pop();

            while (stack.size() != 1) {
                stack.pop();
            }

            answer += stack.pop() - low;
        }
        System.out.println(answer);
    }
}
