package org.example.BF.부분합;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

/**
 * 1 2 3 4 5 6
 * 1 2 3
 * 2 3 4
 * 3 4
 * 2 3 4
 *
 * 현재 수가 낮다 오른쪽 진행
 * 현재 수가 높다 왼쪽 수 빼기
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        int N = Integer.parseInt(temp[0]);
        int M = Integer.parseInt(temp[1]);

        Integer[] nums = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).toArray(Integer[]::new);
        Deque<Integer> deque = new ArrayDeque<>();

        int min = Integer.MAX_VALUE;
        int total = 0;
        for (int i = 0; i < N; i++) {
            if (total + nums[i] >= M) {
                min = Math.min(min, deque.size() + 1);

                if (deque.size() > 0) {
                    total -= deque.removeFirst();
                    i--;
                }
            } else if (total + nums[i] < M) {
                total += nums[i];
                deque.addLast(nums[i]);
            }
        }

        System.out.println(min == Integer.MAX_VALUE ? 0 : min);
    }
}

