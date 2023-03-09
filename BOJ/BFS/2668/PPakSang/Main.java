package org.example.Graph.숫자고르기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 1 3
 * 5 5
 *
 * 1 -> 3
 * 2 -> 1
 * 3 -> 1
 * 4 -> 5
 * 5 -> 5
 * 6 -> 4
 * 7 -> 6
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] pair = new int[N+1];
        for (int i = 1; i <= N; i++) {
            pair[i] = Integer.parseInt(br.readLine());
        }

        int[] cycle = new int[N+1];
        boolean[] visited = new boolean[N+1];
        for (int i = 1; i <= N; i++) {
            if (visited[i]) continue;
            play(i, pair, visited, cycle);
        }

        int result = 0;
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            if (cycle[i]==1) {
                result++;
                sb.append(i);
                sb.append("\n");
            }
        }

        System.out.println(result);
        System.out.println(sb);
    }

    static int play(int s, int[] pair, boolean[] visited, int[] cycle) {
        if (cycle[s] != 0) {
            return -1;
        }
        if (visited[s]) {
            cycle[s] = 1;
            return 1;
        }
        visited[s] = true;

        if (play(pair[s], pair, visited, cycle) == 1) {
            if (cycle[s] == 1) {
                return -1;
            }
            cycle[s] = 1;
            return 1;
        }
        cycle[s] = -1;
        return -1;
    }
}
