package org.example.study.week19.팀빌딩;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * (개발자 A와 개발자 B 사이에 존재하는 다른 개발자 수) × min(개발자 A의 능력치, 개발자 B의 능력치)
 * 개발자 수 100000
 *
 * 4
 * 1 4 2 5
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int max = Integer.MIN_VALUE;
        int left = 0;
        int right = temp.length-1;

        while (left < right) {
            int lV = temp[left];
            int rV = temp[right];

            max = Math.max(max, (right-left-1)*Math.min(lV,rV));

            if (lV < rV) {
                left++;
            } else {
                right--;
            }
        }

        System.out.println(max);
    }
}
