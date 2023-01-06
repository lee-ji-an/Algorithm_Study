package org.example.BF.부분수열의합;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * 001
 * 010
 * 011
 */

public class Main {
    static Set<Integer> naturalNums = new HashSet<>();
    static Integer[] nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        nums = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).toArray(Integer[]::new);

        bitmask(N, 0, "");

        int num = 1;
        while(true) {
            if (!naturalNums.contains(num)) {
                System.out.println(num);
                break;
            }
            num++;
        }
    }

    static void bitmask(int maxCnt, int cnt, String cur) {
        if (maxCnt == cnt) {
            calcScore(cur);
            return;
        }

        bitmask(maxCnt, cnt+1, cur+"0");
        bitmask(maxCnt, cnt+1, cur+"1");
    }

    static void calcScore(String cur) {
        int total = 0;

        for (int i = 0; i < cur.length(); i++) {
            char c = cur.charAt(i);
            if (c == '1') total += nums[i];
        }

        naturalNums.add(total);
    }
}
