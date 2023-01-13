package org.example.BF.두배열의합;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

/**
 * 1 2 3 4 5 6
 * 1 2 3
 * 2 3
 *
 * 3 4
 * 2 3 4
 *
 * A
 * 현재 수가 낮다  (총합 - 현재수) 로 B 진행, A 오른쪽 진행
 * 현재 수가 높거나 같다 왼쪽 수 빼기
 *
 * B
 * 현재 수가 낮다 오른쪽 진행
 * 현재 수가 높다 왼쪽 수 빼기
 * 현재 수가 같다 정답 올리기
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int M = Integer.parseInt(br.readLine());

        int n = Integer.parseInt(br.readLine());
        Integer[] A = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).toArray(Integer[]::new);
        int m = Integer.parseInt(br.readLine());
        Integer[] B = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).toArray(Integer[]::new);
        Map<Integer, Integer> result = new HashMap<>();

        for (int i = 0; i < m; i++) {
            int total = 0;
            for (int j = i; j < m; j++) {
                total += B[j];
                result.put(total, result.getOrDefault(total, 0) + 1);
            }
        }

        long answer = 0;
        for (int i = 0; i < n; i++) {
            int total = 0;
            for (int j = i; j < n; j++) {
                total += A[j];
                answer += result.getOrDefault(M - total, 0);
            }
        }

        System.out.println(answer);
    }
}