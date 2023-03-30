package org.example.study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * 첫째 줄에 지동이의 방에 출입한 모기의 마릿수 N(1 ≤ N ≤ 1,000,000)가 주어진다.
 *
 * 다음 N개의 줄에 모기의 입장 시각 TE과 퇴장 시각 TX이 주어진다. (0 ≤ TE < TX ≤ 2,100,000,000)
 *
 * 모기는 [TE, Tx)동안 존재한다.
 *
 * 3
 * 2 16
 * 4 6
 * 6 10
 *
 * 출발 시간 기준으로 정렬
 * 종료 시간 기준으로 정렬
 *
 * 출발 시간이 더 작으면 넣고
 * 종료 시간이 더 작으면 빼고
 *
 * 구간은 어떻게 정하지, 최댓값 갱신되면?
 * 4,
 *
 * 누적합
 *
 * 3
 * 2 16
 * 4 6
 * 6 10
 *
 * 2 4 6
 * 6 10 16
 * 2 4 6 6
 */


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] inTime = new int[N];
        int[] outTime = new int[N];

        for (int i = 0; i < N; i++) {
            String[] temp = br.readLine().split(" ");
            int in = Integer.parseInt(temp[0]);
            int out = Integer.parseInt(temp[1]);

            inTime[i] = in;
            outTime[i] = out;
        }

        Arrays.sort(inTime);
        Arrays.sort(outTime);

        int inIdx = 0;
        int outIdx = 0;

        int cur = 0;
        int answer = 0;

        int start = 0;
        int end = 0;
        boolean updated = false;
        while (inIdx < N || outIdx < N) {
            if (inIdx == N) {
                if (updated) {
                    end = outTime[outIdx];
                }
                break;
            }

            int t1 = inTime[inIdx];
            int t2 = outTime[outIdx];

            if (t1 < t2) {
                cur++;
                if (answer < cur) {
                    answer = cur;
                    start = t1;
                    updated = true;
                }
                inIdx++;
            }

            if (t1 > t2) {
                cur--;
                if (updated) {
                    updated = false;
                    end = t2;
                }
                outIdx++;
            }

            if (t1 == t2) {
                inIdx++;
                outIdx++;
            }
        }

        System.out.println(answer);
        System.out.println(start + " " + end);
    }
}
