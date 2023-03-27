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

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main2 {
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

        // 첫번째 집과 마지막 집이 같은 색을 칠하지 않도록 하기 위해 시작점을 3가지로 나눠서 계산
        int answer = Integer.MAX_VALUE;
        for (int k = 0; k < 3; k++) {
            int[][] colors = new int[N][3];

            // 시작점 초기화
            for (int i = 0; i < 3; i++) {
                if (i == k) {
                    colors[0][i] = costs[0][i];
                } else {
                    colors[0][i] = 1000 * N;
                }
            }

            // 다음 집부터 색상 계산
            for (int i = 1; i < N; i++) {
                colors[i][0] = costs[i][0] + Math.min(colors[i-1][1], colors[i-1][2]);
                colors[i][1] = costs[i][1] + Math.min(colors[i-1][0], colors[i-1][2]);
                colors[i][2] = costs[i][2] + Math.min(colors[i-1][0], colors[i-1][1]);
            }

            // 종료점 업데이트
            for (int i = 0; i < 3; i++) {
                if (i == k) continue;
                answer = Math.min(answer, colors[N-1][i]);
            }
        }

        System.out.println(answer);
    }
}


