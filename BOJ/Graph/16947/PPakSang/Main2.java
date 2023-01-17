package org.example.Graph.서울지하철2호선;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * 역 갯수 3000개
 * 3000 * 3000 -> 9000000
 * 사이클 다 확인하는거 1천만
 * DFS -> 이번 확인 회차에 이미 방문한 역 도착하면
 *
 * 다시 돌면서 -> 나는 True 인데, 나랑 이어진 애가 False 다 -> +1 하면서
 *
 *
 * 탐색하다가 사이클 발견 ->
 * 탐색하다가 더 갈 수 없음 -> 거기서부터 한칸씩 뒤로 오면서
 */

public class Main2 {
    static List<Integer>[] conn;
    static boolean[] visited;
    static boolean[] onCycle;
    static int[] result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        conn = new List[N];
        onCycle = new boolean[N];
        result = new int[N];

        for (int i = 0; i < N; i++) {
            conn[i] = new ArrayList<>();
        }

        for (int i = 0; i < N; i++) {
            String[] temp = br.readLine().split(" ");
            int s1 = Integer.parseInt(temp[0])-1;
            int s2 = Integer.parseInt(temp[1])-1;
            conn[s1].add(s2);
            conn[s2].add(s1);
        }

        visited = new boolean[N];
        defineCycle(-1, 0);

        visited = new boolean[N];
        Queue<Integer> distance = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            if (onCycle[i]) {
                distance.add(i);
            }
        }
        calcDist(distance);

        StringBuilder sb = new StringBuilder();
        for (int dist : result) {
            sb.append(dist);
            sb.append(" ");
        }

        System.out.println(sb);
    }

    static boolean defineCycle(int prev, int cur) {
        visited[cur] = true;

        boolean cycle = false;
        boolean cycleEnd = false;
        for (int st : conn[cur]) {
            if (prev == st) continue;

            if (visited[st]) {
                onCycle[st] = true;
                cycle = true;
                continue;
            }

            if (defineCycle(cur, st)) {
                if (!onCycle[cur]) {
                    onCycle[cur] = true;
                    cycle = true;
                } else {
                    cycleEnd = true;
                }
            }
        }

        return cycle && !cycleEnd;
    }

    static void calcDist(Queue<Integer> distance) {
        while (distance.size() != 0) {
            int cur = distance.poll();
            visited[cur] = true;

            for (int adj : conn[cur]) {
                if (!visited[adj] && !onCycle[adj]) {
                    result[adj] = result[cur] + 1;
                    distance.add(adj);
                }
            }
        }
    }
}