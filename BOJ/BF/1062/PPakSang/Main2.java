package org.example.BF.가르침;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main2 {
    static boolean[] alpha = new boolean[255];
    static String[] words;
    static int max = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        int N = Integer.parseInt(temp[0]);
        int K = Integer.parseInt(temp[1]);

        words = new String[N];

        alpha['a'] = true;
        alpha['n'] = true;
        alpha['t'] = true;
        alpha['i'] = true;
        alpha['c'] = true;

        for (int i = 0; i < N; i++) {
            words[i] = br.readLine();
        }

        calc(K-5, 0, 'a');

        System.out.println(max);
    }

    static void calc(int maxCnt, int cnt, char cur) {
        if (maxCnt == cnt) {
            max = Math.max(calc2(), max);
            return;
        }

        for (char c = cur; c <= 'z'; c++) {
            if (alpha[c]) continue;

            alpha[c] = true;
            calc(maxCnt, cnt+1, (char)(c+1));
            alpha[c] = false;
        }
    }

    static Integer calc2() {
        int total = 0;
        List<Character> knownChars = new ArrayList<>();

        for (char c = 'a'; c <= 'z'; c++) {
            if (alpha[c]) knownChars.add(c);
        }

        for (String word : words) {
            String check = word;
            for (char c : knownChars) {
                check = check.replaceAll(Character.toString(c), "");
            }
            if (check.length() == 0) total++;
        }

        return total;
    }
}
