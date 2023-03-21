package org.example.study.Graph.궁금한민호;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 1 -> 3 이 1 -> 2 -> 3 이랑 같으면 1 -> 3 은 있을 필요 없다
 *
 * 들렀다 가기 vs 그냥 가기 (더 작은 경로는 있을 필요가 없다)
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[][] dist = new int[N][N];
        for (int i = 0; i < N; i++) {
            String[] temp = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                dist[i][j] = Integer.parseInt(temp[j]);
            }
        }

        for (int k = 0; k < N; k++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (dist[i][j] > dist[i][k] + dist[k][j]) {
                        System.out.println(-1);
                        return;
                    }
                }
            }
        }

        int answer = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                boolean flag = false;
                for (int k = 0; k < N; k++) {
                    if (i != k && j != k && dist[i][j] >= dist[i][k] + dist[k][j]) {
                        flag = true;
                        break;
                    }
                }
                if (!flag) {
                    answer += dist[i][j];
                }
            }
        }

        System.out.println(answer/2);
    }
}
