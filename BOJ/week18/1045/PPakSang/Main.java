package org.example.study.week18.도로;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * 집합에 하나씩 넣다가
 * 도로의 갯수 만큼 뽑았는데 모든 그룹 안찼으면
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");

        int N = Integer.parseInt(temp[0]);
        int M = Integer.parseInt(temp[1]);

        if (N == 1) {
            System.out.println(0);
            return;
        }

        group = new int[N];
        for (int i = 0; i < group.length; i++) {
            group[i] = i;
        }

        List<Edge> edges = new ArrayList<>();

        for (int i = 0; i < N-1; i++) {
            String str = br.readLine();
            for (int j = i + 1; j < str.length(); j++) {
                char c = str.charAt(j);
                if (c == 'Y') {
                    Edge e = new Edge(i, j, false);
                    edges.add(e);
                }
            }
        }

        if (edges.size() < N-1) {
            System.out.println(-1);
            return;
        }

        int cnt = 0;
        for (int i = 0; i < edges.size(); i++) {
            Edge e = edges.get(i);
            if (find(e.n1) == find(e.n2)) continue;
            union(e.n1, e.n2);
            e.selected = true;
            cnt++;
        }

        if (cnt < N-1) {
            System.out.println(-1);
            return;
        }

        cnt = M - cnt;
        for (int i = 0; i < edges.size(); i++) {
            if (cnt == 0) break;
            Edge e = edges.get(i);
            if (e.selected) continue;
            e.selected = true;
            cnt--;
        }

        if (cnt != 0) {
            System.out.println(-1);
            return;
        }

        int[] nums = new int[N];
        for (int i = 0; i < edges.size(); i++) {
            Edge e = edges.get(i);
            if (e.selected) {
                nums[e.n1]++;
                nums[e.n2]++;
            }
        }

        for (int i = 0; i < N; i++) {
            System.out.print(nums[i] + " ");
        }
    }

    static class Edge {
        int n1;
        int n2;
        boolean selected;

        Edge(int n1, int n2, boolean selected) {
            this.n1 = n1;
            this.n2 = n2;
            this.selected = selected;
        }
    }

    static int[] group;
    public static int find(int n1) {
        if (group[n1] == n1) return n1;
        return group[n1] = find(group[n1]);
    }

    public static void union(int n1, int n2) {
        int g1 = find(n1);
        int g2 = find(n2);
        group[g1] = g2;
    }
}
