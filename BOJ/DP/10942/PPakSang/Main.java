package org.example.DP.팰린드롬;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * 1 2 1 3 1 2 1
 * N ~ M 이 팰린드롬 이려면 N == M 이고 N+1 M-1 이 팰린드롬 이여야한다
 *
 */


public class Main {
    static int[][] visited;
    static int[] nums;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        visited = new int[N+1][N+1];
        nums = new int[N+1];

        String[] temp = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            nums[i+1] = Integer.parseInt(temp[i]);
        }

        int M = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            temp = br.readLine().split(" ");
            int left = Integer.parseInt(temp[0]);
            int right = Integer.parseInt(temp[1]);

            int result = dfs(left, right);
            sb.append(result == 1 ? result : 0);
            sb.append("\n");
        }

        System.out.println(sb);
    }

    static int dfs(int left, int right) {
        if (nums[left] != nums[right]) return visited[left][right] = -1;

        if (left == right) return visited[left][right] = 1;
        if (left > right) return 1;

        if (visited[left][right] != 0) return visited[left][right];

        if (dfs(left+1, right-1) == 1) return visited[left][right] = 1;
        else return visited[left][right] = -1;
    }
}
