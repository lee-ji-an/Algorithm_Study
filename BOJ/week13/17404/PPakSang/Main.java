package org.example.study.DP.RGB거리2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 110
 *
 * 3
 * 26 40 83
 * 49 60 57
 * 13 89 99
 *
 * c a b c
 * 빨 a b 빨
 *
 * a 에 빨강 칠할 때 -> 그 전 노랑, 초록 칠한 값 중에 더 작은 값 + 빨강
 * 나머지 색도 똑같이
 *
 * 13 40 57
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[][] costs = new int[N][3];

        for (int i = 0; i < N; i++) {
            String[] temp = br.readLine().split(" ");
            costs[i][0] = Integer.parseInt(temp[0]);
            costs[i][1] = Integer.parseInt(temp[1]);
            costs[i][2] = Integer.parseInt(temp[2]);
        }

        // 빨 주/노  로 시작하면 N 번째는 주, 노 칠할때만 본다
        int[][] colors = new int[N+1][3];

        int answer = Integer.MAX_VALUE;


        colors[0][0] = costs[N-1][0];
        colors[1][0] = 5000;
        colors[1][1] = colors[0][0] + costs[0][1];
        colors[1][2] = colors[0][0] + costs[0][2];
        for (int i = 2; i < N; i++) {
            colors[i][0] += costs[i-1][0] + Math.min(colors[i-1][1], colors[i-1][2]);
            colors[i][1] += costs[i-1][1] + Math.min(colors[i-1][0], colors[i-1][2]);
            colors[i][2] += costs[i-1][2] + Math.min(colors[i-1][0], colors[i-1][1]);
        }

        answer = Math.min(answer, Math.min(colors[N-1][1], colors[N-1][2]));

        colors = new int[N+1][3];
        colors[0][1] = costs[N-1][1];
        colors[1][1] = 5000;
        colors[1][0] = colors[0][1] + costs[0][0];
        colors[1][2] = colors[0][1] + costs[0][2];
        for (int i = 2; i < N; i++) {
            colors[i][0] += costs[i-1][0] + Math.min(colors[i-1][1], colors[i-1][2]);
            colors[i][1] += costs[i-1][1] + Math.min(colors[i-1][0], colors[i-1][2]);
            colors[i][2] += costs[i-1][2] + Math.min(colors[i-1][0], colors[i-1][1]);
        }

        answer = Math.min(answer, Math.min(colors[N-1][0], colors[N-1][2]));

        colors = new int[N+1][3];
        colors[0][2] = costs[N-1][2];
        colors[1][2] = 5000;
        colors[1][1] = colors[0][2] + costs[0][1];
        colors[1][0] = colors[0][2] + costs[0][0];
        for (int i = 2; i < N; i++) {
            colors[i][0] += costs[i-1][0] + Math.min(colors[i-1][1], colors[i-1][2]);
            colors[i][1] += costs[i-1][1] + Math.min(colors[i-1][0], colors[i-1][2]);
            colors[i][2] += costs[i-1][2] + Math.min(colors[i-1][0], colors[i-1][1]);
        }

        answer = Math.min(answer, Math.min(colors[N-1][0], colors[N-1][1]));

        System.out.println(answer);
    }
}
