package org.example.study.week16.꿈틀꿈틀호석애벌레;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 누적합
 * dp
 * 1 5
 * 4
 *
 * 1 2 3 4 5
 *
 * 더하다 넘쳤을 때, 앞에거 빼는게 이득인지 / 그대로 끝내는게 이득인지
 *
 *
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        int N = Integer.parseInt(temp[0]);
        int K = Integer.parseInt(temp[1]);

        temp = br.readLine().split(" ");
        int[] nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(temp[i]);
        }

        long[] dp = new long[N];
        int prev = 0;
        long sum = 0;
        for (int i = 0; i < N; i++) {
            sum += nums[i];
            dp[i] = prev == 0 ? 0 : dp[i-1];
            while (sum >= K) {
                long prevSum = prev == 0L ? 0L : dp[prev-1];
                dp[i] = Math.max(dp[i], prevSum + sum - K);
                sum -= nums[prev++];
            }
        }
        System.out.println(dp[N-1]);
    }
}
