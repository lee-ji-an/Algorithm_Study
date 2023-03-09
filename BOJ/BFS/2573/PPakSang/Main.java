package org.example.bfs_dfs.빙산;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/**
 * 5 7
 * 0 0 0 0 0 0 0
 * 0 2 4 5 3 0 0
 * 0 3 0 2 5 2 0
 * 0 7 6 2 4 0 0
 * 0 0 0 0 0 0 0
 */

public class Main {
    static int N;
    static int M;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");

        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);

        int[][] map = new int[N][M];
        for (int i = 0; i < N; i++) {
            temp = br.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(temp[j]);
            }
        }

        int result = 0;
        while (melt(map)) {
            result++;
            if (!isOverTwo(map)) {
                continue;
            }

            System.out.println(result);
            return;
        }

        System.out.println(0);
    }

    static boolean melt (int[][] map) {
        boolean result = false;
        int[][] arr = new int[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 0) { continue; }
                result = true;
                arr[i][j] = map[i][j] - doMelt(map, i, j);
                if (arr[i][j] < 0) {
                    arr[i][j] = 0;
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                map[i][j] = arr[i][j];
            }
        }

        return result;
    }

    static boolean isOverTwo (int[][] map) {
        boolean[][] visited = new boolean[N][M];

        boolean result = false;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 0 || visited[i][j]) { continue; }
                if (result) return true;
                checkGroup(map, visited, i, j);
                result = true;
            }
        }
        return false;
    }

    static void checkGroup(int[][] map, boolean[][] visited, int x, int y) {
        Queue<Position> q = new LinkedList<>();
        q.add(new Position(x, y));
        visited[x][y] = true;

        while (q.size() > 0) {
            Position cur = q.poll();
            for (int i = 0; i < 4; i++) {
                int nX = cur.x + dirX[i];
                int nY = cur.y + dirY[i];

                if (!inRange(nX, nY) || map[nX][nY] == 0 || visited[nX][nY]) continue;
                visited[nX][nY] = true;
                q.add(new Position(nX, nY));
            }
        }
    }

    static class Position {
        int x;
        int y;

        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int[] dirX = new int[]{1, -1, 0, 0};
    static int[] dirY = new int[]{0, 0, 1, -1};
    static int doMelt(int[][] map, int x, int y) {
        int result = 0;
        for (int i = 0; i < 4; i++) {
            int nX = x + dirX[i];
            int nY = y + dirY[i];

            if (!inRange(nX, nY) || map[nX][nY] > 0) continue;
            result++;
        }
        return result;
    }

    static boolean inRange(int x, int y) {
        if (x < 0 || x >= N) return false;
        if (y < 0 || y >= M) return false;
        return true;
    }
}
