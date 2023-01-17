package org.example.Graph.DFS스페셜저지;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 *
 * 한 뎁스 내려갈 때마다 연결된 String 확인 하면서
 * abcd
 */

public class Main {
    static Set<Integer>[] conn;
    static Integer[] target;
    static int N;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        conn = new Set[N+1];
        visited = new boolean[N+1];

        for (int i = 0; i <= N; i++) {
            conn[i] = new HashSet<>();
        }

        for (int i = 1; i < N; i++) {
            String[] temp = br.readLine().split(" ");
            int n1 = Integer.parseInt(temp[0]);
            int n2 = Integer.parseInt(temp[1]);

            conn[n1].add(n2);
            conn[n2].add(n1);
        }

        target =  Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).toArray(Integer[]::new);
        int result = calcMaxLength(target[0], 1);

        System.out.println(result == N && target[0] == 1?1:0);
    }

    static int calcMaxLength(Integer n, int cnt) {
        if (cnt == N) return 1;

        int prev = cnt;
        int k = conn[n].size();

        while (k > 0 && cnt != N) {
            if (!conn[n].contains(target[cnt])) return cnt - prev + 1;
            cnt += calcMaxLength(target[cnt], cnt+1);
            k--;
        }
        return cnt - prev + 1;
    }
}
