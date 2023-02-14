package org.example.simulation.인구이동;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * 국경 이동 안한 국가 선택, 이동할 수 있는 곳 전부 마킹, 분할 인구 픽스 박고 마킹한 곳 돌면서 초기화
 */

public class Main {
    static int N;
    static int L;
    static int R;

    static int[][] map;

    static int[] dirX = new int[]{1, -1, 0, 0};
    static int[] dirY = new int[]{0, 0, 1, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");

        N = Integer.parseInt(temp[0]);
        L = Integer.parseInt(temp[1]);
        R = Integer.parseInt(temp[2]);

        map = new int[N][N];
        for (int i = 0; i < N; i++) {
            temp = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(temp[j]);
            }
        }

        int answer = 0;
        while (true) {
            boolean result = false;
            boolean[][] visited = new boolean[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (!visited[i][j]) result |= bfs(visited, i, j);
                }
            }
            if (!result) break;
            answer++;
        }

        System.out.println(answer);
    }

    static boolean bfs(boolean[][] visited, int sX, int sY) {
        Queue<Position> q = new LinkedList<>();
        q.add(new Position(sX, sY));

        List<Position> visitedP = new ArrayList<>();
        visitedP.add(new Position(sX, sY));
        visited[sX][sY] = true;
        int sum = map[sX][sY];

        while (q.size() > 0) {
            Position cur = q.poll();

            for (int i = 0; i < 4; i++) {
                int nX = cur.x + dirX[i];
                int nY = cur.y + dirY[i];

                if (checkRange(nX, nY) && !visited[nX][nY] && diff(cur.x, cur.y, nX, nY)) {
                    sum += map[nX][nY];
                    visited[nX][nY] = true;
                    Position next = new Position(nX, nY);
                    visitedP.add(next);
                    q.add(next);
                }
            }
        }

        int move = sum/visitedP.size();
        for (Position p : visitedP) {
            map[p.x][p.y] = move;
        }

        return visitedP.size() > 1;
    }

    private static boolean diff(int x, int y, int nX, int nY) {
        int diff = Math.abs(map[x][y] - map[nX][nY]);
        return diff >= L && diff <= R;
    }

    private static boolean checkRange(int nX, int nY) {
        if (nY < 0 || nY >= N) return false;
        if (nX < 0 || nX >= N) return false;
        return true;
    }

    static class Position {
        int x;
        int y;

        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
