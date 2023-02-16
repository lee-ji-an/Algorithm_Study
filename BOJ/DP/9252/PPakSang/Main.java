package org.example.DP.LCS2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word1 = br.readLine();
        String word2 = br.readLine();

        int N = word1.length();
        int M = word2.length();
        int[][] lcs = new int[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                char c1 = word1.charAt(i);
                char c2 = word2.charAt(j);

                int n1 = i - 1 < 0 ? 0 : lcs[i-1][j];
                int n2 = j - 1 < 0 ? 0 : lcs[i][j-1];
                int num = 0;
                if (c1 == c2) {
                    num = i - 1 < 0 || j -1 < 0 ? 1 : lcs[i-1][j-1]+1;
                }
                lcs[i][j] = Math.max(num, Math.max(n1, n2));
            }
        }

        int result = lcs[N-1][M-1];
        int i = N-1;
        int j = M-1;

        StringBuilder sb = new StringBuilder();
        while (true) {
            while (i > 0) {
                if (lcs[i-1][j] == result) {
                    i--;
                    continue;
                }
                break;
            }
            while (j> 0) {
                if (lcs[i][j-1] == result) {
                    j--;
                    continue;
                }
                break;
            }
            if (lcs[i][j] != 0) sb.insert(0, word1.charAt(i));
            i--;
            j--;
            if (i < 0 || j < 0) break;
            result--;
        }

        System.out.println(lcs[N-1][M-1]);
        System.out.println(sb);

    }
}
