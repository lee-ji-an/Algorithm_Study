package org.example.BF.연산자끼워넣기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int[] operators;
    static int[] nums;

    static int maxAnswer = Integer.MIN_VALUE;
    static int minAnswer = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());


        nums = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        operators = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();;

        permutation(1, N, nums[0]);
        System.out.println(maxAnswer);
        System.out.println(minAnswer);
    }

    static void permutation(int cnt, int max, int num) {
        if (cnt == max) {
            maxAnswer = Math.max(maxAnswer, num);
            minAnswer = Math.min(minAnswer, num);
            return;
        }

        for (int i = 0; i < 4; i++) {
            if(operators[i] == 0) continue;
            operators[i]--;
            switch (i) {
                case 0: permutation(cnt+1, max, num + nums[cnt]); break;
                case 1: permutation(cnt+1, max, num - nums[cnt]); break;
                case 2: permutation(cnt+1, max, num * nums[cnt]); break;
                case 3: permutation(cnt+1, max, num / nums[cnt]); break;
            }
            operators[i]++;
        }
    }
}
