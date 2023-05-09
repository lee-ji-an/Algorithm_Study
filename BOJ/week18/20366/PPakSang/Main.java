package org.example.study.week18.같이눈사람만들래;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;


/**
 * 눈 4개
 * 360000
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] temp = br.readLine().split(" ");

        int[] nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(temp[i]);
        }

        List<int[]> answer = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                answer.add(new int[]{nums[i]+nums[j], i, j});
            }
        }

        answer.sort((i1, i2) -> i1[0] - i2[0]);

        int ans = Integer.MAX_VALUE;
        for (int i = 1; i < answer.size(); i++) {
            int[] num1 = answer.get(i);
            int[] num2 = answer.get(i-1);

            if (num1[1] == num2[1] || num1[1] == num2[2] || num1[2] == num2[1] || num1[2] == num2[2]) continue;
            ans = Math.min(ans, num1[0]-num2[0]);
        }

        System.out.println(ans);
    }
}
