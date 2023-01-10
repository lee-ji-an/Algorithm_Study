package org.example.BF.가르침;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * anta tica, ant ic 최소 5개
 * rc, hello, car  rc, helo, car
 * 그냥 모든 알파벳 중에 K 개 뽑고
 */

public class Main {
    static boolean[] alpha = new boolean[255];
    static Integer[] words;
    static int max = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        int N = Integer.parseInt(temp[0]);
        int K = Integer.parseInt(temp[1]);

        words = new Integer[N];
        for (int i = 0; i < N; i++) {
            words[i] = 0;
        }

        alpha['a'] = true;
        alpha['n'] = true;
        alpha['t'] = true;
        alpha['i'] = true;
        alpha['c'] = true;

        for (int i = 0; i < N; i++) {
            String word = br.readLine();
            for (int j = 0; j < word.length(); j++) {
                words[i] |= 1<<(word.charAt(j)-'a');
            }
        }

        teach(K-5, 0, 'a');

        System.out.println(max);
    }

    static void teach(int maxCnt, int cnt, char cur) {
        if (maxCnt == cnt) {
            max = Math.max(calc(), max);
            return;
        }

        for (char c = cur; c <= 'z'; c++) {
            if (alpha[c]) continue;

            alpha[c] = true;
            teach(maxCnt, cnt+1, (char)(c+1));
            alpha[c] = false;
        }
    }

    static Integer calc() {
        int total = 0;
        int knownChar = 0;

        for (char c = 'a'; c <= 'z'; c++) {
            if (alpha[c]) knownChar |= 1<<(c - 'a');
        }

        for (Integer word : words) {
            if ((word & knownChar) == word) total++;
        }

        return total;
    }
}
