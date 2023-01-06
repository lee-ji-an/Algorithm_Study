package org.example.BF.부분수열의합;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main2 {
    static Set<Integer> naturalNums = new HashSet<>();
    static Integer[] nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        nums = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).toArray(Integer[]::new);

        for (int i = 0; i < (1<<N); i++) {
            int sum = 0;
            for (int j = 0; j < N; j++) {
                if ((i & (1<<j)) != 0) {
                    sum += nums[j];
                }
            }
            naturalNums.add(sum);
        }

        int num = 1;
        while(true) {
            if (!naturalNums.contains(num)) {
                System.out.println(num);
                break;
            }
            num++;
        }
    }
}
