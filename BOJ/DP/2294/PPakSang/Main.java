package org.example.DP.동전2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");

        int n = Integer.parseInt(temp[0]);
        int k = Integer.parseInt(temp[1]);

        int[] sum = new int[k+1];
        int[] coins = new int[n];
        for (int i = 0; i < n; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }

        Arrays.fill(sum, 10001);
        sum[0] = 0;
        for (int coin : coins) {
            for (int i = coin; i <= k; i++) {
                sum[i] = Math.min(sum[i-coin]+1, sum[i]);
            }
        }

        System.out.println(sum[k] == 10001 ? -1 : sum[k]);
    }
}
