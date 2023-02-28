package org.example.simulation.레벨햄버거;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 레벨-0 버거는 패티만으로 이루어져 있다.
 * 레벨-L 버거는 햄버거번, 레벨-(L-1) 버거, 패티, 레벨-(L-1)버거, 햄버거번으로 이루어져 있다. (L ≥ 1)
 *
 * P ... 1 (0, 1)
 * B P P P B ... 2 (1+num[1]+1+num[1]+1) (1, 3)
 * B BPPPB P BPPPB B ... 3 (7) (2, 7)
 * B BBPPPBPBPPPBB P BBPPPBPBPPPBB B
 *
 * 1 -> 1 5 13 29 Num[N] = 2*Num[N-1]+3
 * 1 3 7 2N+1
 *
 * 5
 * 1 = 0
 * 2 = 1
 * 3 = 2
 * 4 = 3
 * 5 = 3
 * bugger[L][N]
 * N == 1 -> L == 1 ? 1 : 0
 * N 이 2 ~ 1+num[i-1] -> N개 먹으면 bugger[L-1][N-1]
 * N 이 2+num[i-1] -> bugger[L-1][N-1] + 1
 * 2+num[i-1]+1 ~ 2 + 2*num[i-1] ->  bugger[L-1][num[L-1]] + 1 + bugger[L][N-num[L-1]+2]
 * 3 + 2*num[i-1] -> bugger[L][N-1]
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");

        int L = Integer.parseInt(temp[0]);
        long N = Long.parseLong(temp[1]);

        long[] num = new long[L+1];
        long[] pNum = new long[L+1];

        num[0] = 1;
        pNum[0] = 1;
        for (int i = 1; i < L+1; i++) {
            num[i] = 2*num[i-1] + 3;
            pNum[i] = 2*pNum[i-1] + 1;
        }

        System.out.println(bugger(L, N, num, pNum));
    }

    static long bugger(int L, long N, long[] num, long[] pNum) {
        if (N == 1) {
            return L == 0 ? 1 : 0;
        }
        else if (2 <= N && N <= 1+num[L-1]) {
            return bugger(L-1, N-1, num, pNum);
        }
        else if (N == 2+num[L-1]) {
            return pNum[L-1] + 1;
        }
        else if (2+num[L-1]+1 <= N && N <= 2+2*num[L-1]) {
            return pNum[L-1] + 1 + bugger(L-1, N-num[L-1]-2, num, pNum);
        }
        else if (N == 3+2*num[L-1]){
            return pNum[L-1] + 1 + bugger(L-1, N-num[L-1]-3, num, pNum);
        }

        return Long.MAX_VALUE;
    }
}
