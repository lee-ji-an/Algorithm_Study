package org.example.BF.부분수열의합_easy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int[] nums;
    static int target;
    static int answer = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        int N = Integer.parseInt(temp[0]);
        target = Integer.parseInt(temp[1]);

        nums = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        combination(0, N, 0);
        System.out.println(target == 0 ? answer-1:answer);
    }

    static void combination(int cur, int max, int sum) {
        if (cur == max) {
            if (sum == target) answer++;
            return;
        }

        combination(cur+1, max, sum+nums[cur]);
        combination(cur+1, max, sum);
    }
}

