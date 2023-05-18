package org.example.study.week19.오타;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

/**
 * ()(())))
 *
 * (((())()
 *
 * ((
 *
 * ))
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        Stack<Brace> stack = new Stack<>();
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            Brace b = new Brace(i, c);

            if (stack.isEmpty()) {
                stack.push(b);
                continue;
            }

            if (c == ')') {
                if (stack.peek().c == '(') {
                    stack.pop();
                    continue;
                }
            }
            stack.push(b);
        }

        if (stack.size() != 2) {
            System.out.println(0);
            return;
        }

        Brace b1 = stack.pop();
        Brace b2 = stack.pop();
        System.out.println(b1.idx);
        System.out.println(b2.idx);

        int cnt = 0;
        if (b1.c == '(') {
            for (int i = b1.idx; i < str.length(); i++) {
                if (str.charAt(i) == '(') cnt++;
            }
        } else {
            for (int i = b2.idx; i >= 0; i--) {
                if (str.charAt(i) == ')') cnt++;
            }
        }

        System.out.println(cnt);
    }
//
    static class Brace {
        int idx;
        char c;

        Brace(int idx, char c) {
            this.idx = idx;
            this.c = c;
        }
    }
}
