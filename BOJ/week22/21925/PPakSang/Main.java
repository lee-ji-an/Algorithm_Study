package org.example.study.week22.짝수팰린드롬;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.Arrays;

/**
 * 짝 팰 찾고, 나머지에서 짝팰 -> Max
 * 25000000
 * dp[i] -> i 이하의 수열 중 짝수 팰린드롬 최대 수
 *
 *
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        nums = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        dp = new int[N];

        System.out.println(calc(0, N-1));
    }

    static int[] dp;
    static int[] nums;
    static int calc(int left, int right) {
        if (((right-left+1) % 2) != 0 || left == right) {
            return -1;
        }

        if (left > right) {
            return 0;
        }

        if (dp[left] != 0) {
            return dp[left];
        }

        int idx;
        for (int i = 1; i <= (right-left)/2 + 1; i++) {
            idx = left+i;
            if (idx > right) break;
            for (int j = 1; j <= i; j++) {
                if (nums[idx- (2*(j-1) + 1)] != nums[idx]) {
                    break;
                }

                idx++;
                if (j == i) {
                    int res = calc(idx, right);
                    if (res == -1) break;
                    dp[left] = Math.max(dp[left], 1 + res);
                }
            }
        }

        if (dp[left] == 0) {
            dp[left] = -1;
        }
        return dp[left];
    }
}
