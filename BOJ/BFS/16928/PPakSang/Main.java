package org.example.bfs.뱀과사다리게임;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/**
 * 차례 마다 위치를 Queue 에 삽입
 * 빼서 쓰다가 100에 도착하면 게임 끝
 */

public class Main {
    static int[] route = new int[101];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");
        int routeNums = Integer.parseInt(temp[0]) + Integer.parseInt(temp[1]);
        for (int i = 0; i < routeNums ; i++){
            temp = br.readLine().split(" ");
            route[Integer.parseInt(temp[0])] = Integer.parseInt(temp[1]);
        }

        Position result = bfs(new Position(1, 0));

        System.out.println(result.cnt);
    }

    static Position bfs(Position start) {
        Queue<Position> q = new LinkedList<>();
        boolean[] visited = new boolean[101];
        visited[start.pos] = true;
        q.add(start);

        while (q.size() > 0) {
            Position cur = q.poll();
            if (cur.pos == 100) return cur;

            for (int i = 1; i <= 6; i++) {
                int nextPos = cur.pos + i;
                int usingRoutePos = route[nextPos];

                if (nextPos > 100) continue;
                if (visited[nextPos]) continue;

                if (usingRoutePos != 0) {
                    visited[nextPos] = true;
                    visited[usingRoutePos] = true;
                    q.add(new Position(usingRoutePos, cur.cnt + 1));
                } else {
                    visited[nextPos] = true;
                    q.add(new Position(nextPos, cur.cnt + 1));
                }
            }
        }

        throw new RuntimeException();
    }

    static class Position {
        int pos;
        int cnt;

        public Position(int pos, int cnt) {
            this.pos = pos;
            this.cnt = cnt;
        }
    }
}