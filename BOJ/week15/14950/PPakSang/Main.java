package org.example.study.week15.정복자;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

/**
 * 4 5 8
 * 1 2 3
 * 1 3 2
 * 2 3 2
 * 2 4 4
 * 3 4 1
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");

        int N = Integer.parseInt(temp[0]);
        int M = Integer.parseInt(temp[1]);
        int t = Integer.parseInt(temp[2]);

        PriorityQueue<Edge> pq = new PriorityQueue<>((n1, n2) -> {
            return n1.w - n2.w;
        });

        for (int i = 0; i < M; i++) {
            temp = br.readLine().split(" ");
            int n1 = Integer.parseInt(temp[0]);
            int n2 = Integer.parseInt(temp[1]);
            int w = Integer.parseInt(temp[2]);

            pq.add(new Edge(n1, n2, w));
        }

        int[] group = new int[N+1];
        for (int i = 0; i <= N; i++) {
            group[i] = i;
        }

        int answer= 0;
        while (pq.size() > 0) {
            Edge e = pq.poll();
            int g1 = find(e.n1, group);
            int g2 = find(e.n2, group);

            if (g1 == g2) continue;
            union(g1, g2, group);
            answer += e.w;
        }

        if (N == 1) {
            System.out.println(0);
            return;
        }
        System.out.println(answer + t*(N-1)*(N-2)/2);
    }

    static int find(int n1, int[] group) {
        if (group[n1] == n1) return n1;
        return group[n1] = find(group[n1], group);
    }

    static void union(int n1, int n2, int[] group) {
        int g1 = find(n1, group);
        int g2 = find(n2, group);
        group[g1] = g2;
    }

    static class Edge {
        int n1;
        int n2;
        int w;
        Edge(int n1, int n2, int w) {
            this.n1 = n1;
            this.n2 = n2;
            this.w = w;
        }
    }
}
