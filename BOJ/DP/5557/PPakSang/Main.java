package org.example.DP.일학년;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int[] nums;
    static int answer;
    static long[][] game;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        nums = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        answer = nums[n-1];
        game = new long[n-1][21];

        System.out.println(dfs(1, n-1, nums[0]));
    }

    static long dfs(int cur, int max, int num) {
        if (num < 0 || num > 20) return 0;
        if (cur == max) {
            if (num == answer) return 1;
            return 0;
        }
        if (game[cur][num] != 0) return game[cur][num];

        return game[cur][num] = dfs(cur+1, max, num+nums[cur]) + dfs(cur+1, max, num-nums[cur]);
    }
}
