package org.example.study.week17.IPv6;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * ::
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        String[] temp = input.split(":");

        int last = 0;
        if (input.substring(input.length()-2).equals("::")) {
            last = 8 - temp.length;
        }

        int cnt = 8;
        for (int i = 0; i < temp.length; i++) {
            String s = temp[i];
            if (s.length() == 0) continue;
            cnt--;
            String str = "0".repeat(4-s.length()) + s;
            temp[i] = str;
        }

        StringBuilder sb = new StringBuilder();
        boolean done = false;
        for (String s : temp) {
            if (s.length() == 0) {
                if (!done) {
                    for (int i = 0; i < cnt; i++) {
                        sb.append("0000:");
                    }
                    done = true;
                }
                continue;
            }
            sb.append(s+":");
        }

        for (int i = 0; i < last; i++) {
            sb.append("0000:");
        }
        String answer = sb.toString();
        System.out.println(answer.substring(0, answer.length()-1));
    }
}
