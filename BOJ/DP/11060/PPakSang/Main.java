package org.example.DP.점프점프;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 각 칵에서 갈 수 있는 최대 칸 마킹, 최댓값이 갱신된다 -> 횟수 증가
 * 갈 수 있는 칸이 끝났는데 0 나온다 -> -1
 * 갈 수 있는 칸이 최댓값을 넘어간다 -> 그 때 값 출력
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] visited = new int[N];
        String[] temp = br.readLine().split(" ");

        if (N == 1) {
                System.out.println(0);
                return;
        }

        int max = 0;
        for (int i = 0; i < N; i++) {
            int jump = Integer.parseInt(temp[i]);
            if (max < i) {
                System.out.println(-1);
                return;
            }
            if (max < i+jump) {
                if (i+jump >= N - 1) {
                    System.out.println(visited[i]+1);
                    return;
                }
                for (int j = max+1; j <= i+jump; j++) {
                    visited[j] = visited[i] + 1;
                }
                max = i+jump;
            }
        }
    }
}
