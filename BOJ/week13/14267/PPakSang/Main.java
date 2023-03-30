package org.example.study.tree.회사문화;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * 5 3
 * -1 1 2 3 4
 * 2 2
 * 3 4
 * 5 6
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");

        int n = Integer.parseInt(temp[0]);
        int m = Integer.parseInt(temp[1]);

        temp = br.readLine().split(" ");

        List<Integer>[] hierarchy = new List[n+1];
        int[] compliment = new int[n+1];

        for (int i = 0; i <= n; i++) {
            hierarchy[i] = new ArrayList<>();
        }

        for (int i = 1; i <= n; i++) {
            int high = Integer.parseInt(temp[i-1]);

            if (high == -1) {
                continue;
            }

            hierarchy[high].add(i);
        }

        for (int i = 0; i < m; i++) {
            temp = br.readLine().split(" ");
            int to = Integer.parseInt(temp[0]);
            int w = Integer.parseInt(temp[1]);

            compliment[to] += w;
        }

        Queue<Integer> q = new LinkedList<>();
        q.add(1);

        while(q.size() > 0) {
            int president = q.poll();

            for (int sub : hierarchy[president]) {
                compliment[sub] += compliment[president];
                q.add(sub);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            sb.append(compliment[i]);
            sb.append(" ");
        }
        System.out.println(sb);
    }
}
