package org.example.study.week16.밑장빼기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 분배한 사람부터 카드 받기
 * 밑장 빼기 한번
 *
 * 홀수번째 누적합
 * 짝수번째 누적합
 *
 * 1 3 5 7 -> 홀 03
 * 2 4 6 8
 *
 * 첨부터
 * 8 2 4 6 -> 짝 03
 * 1 3 5 7
 *
 * 1
 * 1 8 4 6 -> 홀 0 + 짝 13
 * 2 3 5 7 -> 홀 13 + 짝 0
 *
 * 2
 * 1 3 8 6 -> 홀 01 + 짝 23
 * 2 4 5 7 -> 홀 23 + 짝 01
 *
 * 3
 * 1 3 5 8 -> 홀 02 + 짝 3
 *
 * 1 3 4 7 1 3 7
 * 2 5 6 8
 *
 * 홀 0 1 2 3
 *
 * 상대방한테도 밑장빼기 가능
 *
 *
 * 1 2 4 6 홀0 짝012
 * 8
 *
 * 1 3 4 6 홀01 짝12
 * 2 8 5 7
 *
 * 1 3 5 6 홀012 짝 2
 * 2 4 8 7
 *
 * 0 1
 * 0
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] temp = br.readLine().split(" ");

        int[] sumOdd = new int[N/2];
        int[] sumEven = new int[N/2];
        sumEven[0] = Integer.parseInt(temp[0]);
        sumOdd[0] = Integer.parseInt(temp[1]);
        for (int i = 2; i < N; i++) {
            int num = Integer.parseInt(temp[i]);

            if (i % 2 == 0) {
                sumEven[i/2] = sumEven[i/2 - 1] + num;
            } else {
                sumOdd[i/2] = sumOdd[i/2 - 1] + num;
            }
        }

        int max = sumOdd[N/2-1];
        for (int i = 0; i < N/2; i++) {
            max = Math.max(max, sumEven[i] + (sumOdd[N/2-1] - sumOdd[i]));
            if (N/2 > 1) {
                if (i == 0) {
                    max = Math.max(max, sumEven[i] + (sumOdd[N/2-2]));
                    continue;
                }
                max = Math.max(max, sumEven[i] + (sumOdd[N/2-2] - sumOdd[i - 1]));
            }
        }
        System.out.println(max);
    }
}
