package org.example.study.week17.불우이웃돕기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        List<Edge> edges = new ArrayList<>();
        int total = 0;
        for (int i = 0; i < N; i++) {
            String temp = br.readLine();
            for (int j = 0; j < N; j++) {
                char c = temp.charAt(j);
                int num = 0;
                if (c >= 'a' && c <= 'z') {
                    num = c - 'a' + 1;
                } else if (c >= 'A' && c <= 'Z') {
                    num = c - 'A' + 27;
                }
                total += num;
                if (num != 0)
                    edges.add(new Edge(i, j, num));
            }
        }

        group = new int[N];
        for (int i = 0; i < N; i++) {
            group[i] = i;
        }

        PriorityQueue<Edge> pq = new PriorityQueue<>((e1, e2) -> e1.w - e2.w);
        pq.addAll(edges);
        int answer = 0;
        while (pq.size() > 0) {
            Edge cur = pq.poll();

            int g1 = find(cur.n1);
            int g2 = find(cur.n2);

            if (g1 == g2) {
                continue;
            }

            answer += cur.w;
            union(g1, g2);
        }

        for (int i = 1; i < group.length; i++) {
            if (find(i) != find(i-1)) {
                System.out.println(-1);
                return;
            }
        }

        System.out.println(total-answer);
    }

    static int[] group;
    static void union(int n1, int n2) {
        int g1 = find(n1);
        int g2 = find(n2);

        group[g1] = g2;
    }
    static int find(int n1) {
        if (group[n1] == n1) return n1;
        return group[n1] = find(group[n1]);
    }

    static class Edge {
        int n1;
        int n2;
        int w;

        Edge (int n1, int n2, int w) {
            this.n1 = n1;
            this.n2 = n2;
            this.w = w;
        }
    }
}
