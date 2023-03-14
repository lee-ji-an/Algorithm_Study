package org.example.study.tree.트리의지름;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * 1. 왼쪽, 오른쪽 엣지 포함 -> 내가 루트,
 * 2. 왼쪽 엣지만 vs 오른쪽 엣지만
 *
 * 12
 * 1 2 3
 * 1 3 2
 * 2 4 5
 * 3 5 11
 * 3 6 9
 * 4 7 1
 * 4 8 7
 * 5 9 15
 * 5 10 4
 * 6 11 6
 * 6 12 10
 */

public class Main {
    static int answer = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        List<Edge>[] conn = new List[N+1];

        for (int i = 0 ; i < N+1; i++) {
            conn[i] = new ArrayList<>();
        }

        for (int i = 0; i < N-1; i++) {
            String[] temp = br.readLine().split(" ");
            int r = Integer.parseInt(temp[0]);
            int c = Integer.parseInt(temp[1]);
            int w = Integer.parseInt(temp[2]);

            conn[r].add(new Edge(c, w));
        }

        conn[0].add(new Edge(1, 0));
        int result = play(conn, 0, 0);
        answer = Math.max(answer, result);
        System.out.println(answer);
    }

    static int play (List<Edge>[] conn, int start, int prev) {
        int cNum = conn[start].size();
        if (cNum == 0) {
            return prev;
        } else if (cNum == 1) {
            Edge left = conn[start].get(0);
            return play(conn, left.n, prev + left.w);
        }

        List<Integer> answers = new ArrayList<>();
        for (Edge edge : conn[start]) {
            answers.add(play(conn, edge.n, prev + edge.w));
        }
        answers.sort(Comparator.reverseOrder());

        answer = Math.max(answer, (answers.get(0) - prev) + (answers.get(1) - prev));
        return answers.get(0);
    }

    static class Edge {
        int n;
        int w;

        public Edge(int n, int w) {
            this.n = n;
            this.w = w;
        }
    }
}
