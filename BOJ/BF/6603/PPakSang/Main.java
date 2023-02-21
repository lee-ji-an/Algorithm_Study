package org.example.BF.로또;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String[] temp = br.readLine().split(" ");
            int K = Integer.parseInt(temp[0]);

            if (K == 0) break;
            int[] nums = Arrays.stream(Arrays.copyOfRange(temp, 1, temp.length)).mapToInt(Integer::parseInt).toArray();

            combination(0, 6, 0, new int[6], nums);
            sb.append("\n");
        }
        System.out.println(sb);
    }

    static void combination(int cur, int max, int prev, int[] visited, int[] nums) {
        if (cur == max) {

            for (int i = 0; i < max; i++) {
                sb.append(visited[i]);
                sb.append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = prev; i < nums.length; i++) {
            visited[cur] = nums[i];
            combination(cur+1, max, i+1, visited, nums);
        }
    }
}
