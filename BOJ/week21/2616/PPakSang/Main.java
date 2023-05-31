package org.example.study.week21.소형기관차;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * 소형 기관차가 최대로 끌 수 있는 객차의 수를 미리 정해 놓고,
 * 그보다 많은 수의 객차를 절대로 끌게 하지 않는다. 3대의 소형 기관차가 최대로 끌 수 있는 객차의 수는 서로 같다.
 *
 * 소형 기관차 3대를 이용하여 최대한 많은 손님을 목적지까지 운송하도록 한다.
 * 각 객차 마다 타고 있는 손님의 수는 미리 알고 있고, 다른 객차로 손님들이 이동하는 것은 허용하지 않는다.
 *
 * 각 소형 기관차는 번호가 연속적으로 이어진 객차를 끌게 한다.
 * 객차는 기관차 바로 뒤에 있는 객차부터 시작하여 1번 부터 차례로 번호가 붙어있다.
 *
 * ---
 * 한 객차 잡으면 수는 정해지고, 누적합
 *
 * 객차 수
 *
 *
 */

public class Main {
    static int constant;
    static int[] choose;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        int[] customers = Arrays.stream((br.readLine().split(" "))).mapToInt(Integer::parseInt).toArray();
        constant = Integer.parseInt(br.readLine());

        choose = new int[customers.length];

        int sum = 0;
        int right = Math.min(constant, customers.length);

        for (int i = 0; i < right; i++) {
            sum += customers[i];
        }
        choose[0] = sum;

        for (int i = 0; i < customers.length-1; i++) {
            sum = sum - customers[i];
            if (right < customers.length) {
                sum += customers[right];
            }
            right++;
            choose[i+1] = sum;
        }

        dp = new int[choose.length][4];

        int answer = 0;
        for (int i = 1; i < 4; i++) {
            for (int j = choose.length-1; j >= 0; j--) {
                int prevMax = 0;
                if (j+constant < dp.length) {
                    prevMax = dp[j+constant][i-1];
                }

                int max = 0;
                if (j+1 < dp.length) {
                    max = dp[j+1][i];
                }

                dp[j][i] = Math.max(max, choose[j] + prevMax);
                answer = Math.max(answer, dp[j][i]);
            }
        }

        System.out.println(answer);
    }
}
