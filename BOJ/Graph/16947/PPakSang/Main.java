package org.example.Graph.서울지하철2호선;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * 역 갯수 3000개
 * 3000 * 3000 -> 9000000
 * 사이클 다 확인하는거 1천만
 * DFS -> 이번 확인 회차에 이미 방문한 역 도착하면
 *
 * 다시 돌면서 -> 나는 True 인데, 나랑 이어진 애가 False 다 -> +1 하면서
 *
 * 탐색하다가 사이클 발견 ->
 * 탐색하다가 더 갈 수 없음 -> 거기서부터 한칸씩 뒤로 오면서
 */

public class Main {
    static List<Integer>[] conn;
    static boolean[] visited;
    static boolean[] onCycle;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        conn = new List[N];
        onCycle = new boolean[N];
        int[] result = new int[N];

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

        for (int i = 0; i < N; i++) {
            if (!onCycle[i]) {
                visited = new boolean[N];
                visited[i] = true;
                for (int st : conn[i]) {
                    if (!visited[st] && calcCycle(i, st, true)) {
                        onCycle[i] = true;
                    }
                }
            }
        }

        for (int i = 0; i < N; i++) {
            if (!onCycle[i]) {
                visited = new boolean[N];
                result[i] = calcDist(i, 0);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int dist : result) {
            sb.append(dist);
            sb.append(" ");
        }

        System.out.println(sb);
    }

    static boolean calcCycle(int start, int cur, boolean isStart) {
        visited[cur] = true;
        boolean cycle = false;

        for (int st : conn[cur]) {
            if (!isStart && start == st) return true;
            if (visited[st]) continue;
            if (calcCycle(start, st, false)) {
                cycle = true;
            }
        }

        if (!onCycle[cur] && cycle) onCycle[cur] = true;
        return cycle;
    }

    static int calcDist(int cur, int cnt) {
        if (onCycle[cur]) return cnt;
        visited[cur] = true;

        int min  = Integer.MAX_VALUE;
        for (int s : conn[cur]) {
            if (visited[s]) continue;
            min = Math.min(min,calcDist(s, cnt+1));
        }

        return min;
    }
}