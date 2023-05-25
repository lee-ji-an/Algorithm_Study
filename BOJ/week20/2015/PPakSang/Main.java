package org.example.study.week20.수들의합4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * 4 0
 * 2 -2 2 -2
 * 2 0 2 0
 *
 * two sum (x) -> 부분합
 *
 * n1 + n2 = k
 * k - n1
 *
 * 0~i - 0~j = k
 *
 * 0~i - k 를 만족하는 0~j 가 있는가
 *
 *
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        int n = Integer.parseInt(temp[0]);
        long k = Integer.parseInt(temp[1]);

        long[] nums = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();
        for (int i = 1; i < nums.length; i++) {
            nums[i] = nums[i] + nums[i-1];
        }

        long cnt = 0;
        Map<Long, Long> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            long num = nums[i];
            if (num == k) cnt++;
            long target = num - k;
            cnt += map.getOrDefault(target, 0L);
            map.put(num, map.getOrDefault(num, 0L)+1);
        }

        System.out.println(cnt);
    }
}
