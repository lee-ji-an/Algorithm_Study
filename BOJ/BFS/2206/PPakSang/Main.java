package org.example.bfs.벽부수고이동하기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/**
 * bfs, 이동 좌표에 마킹
 * 벽 부수고 이동한 것인가, 아닌가
 */

public class Main {

    static int[] dirX = {1, -1, 0, 0};
    static int[] dirY = {0, 0, 1, -1};

    static int N;
    static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);

        int[][] map = new int[N][M];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(Character.toString(line.charAt(j)));
            }
        }

        System.out.println(bfs(map));
    }

    static int bfs(int[][] map) {
        boolean[][][] visited = new boolean[N][M][2];

        Queue<Position> q = new LinkedList<>();
        q.add(new Position(0, 0, 1, false));

        while (q.size() > 0) {
            Position cur = q.poll();

            for (int i = 0; i < 4; i++) {
                int nX = cur.x + dirX[i];
                int nY = cur.y + dirY[i];

                int crashNum = cur.crash ? 1 : 0;

                if (checkRange(nX, nY) && !visited[nX][nY][crashNum]) {
                    if (map[nX][nY] == 1) {
                        if (cur.crash) continue;
                        visited[nX][nY][crashNum] = true;
                        q.add(new Position(nX, nY, cur.cnt+1, true));
                    } else {
                        if (nX == N-1 && nY == M-1) return cur.cnt+1;
                        visited[nX][nY][crashNum] = true;
                        q.add(new Position(nX, nY, cur.cnt+1, cur.crash));
                    }
                }
            }
        }

        return (N == 1 && M == 1) ? 1 : -1;
    }

    static class Position {
        int x;
        int y;
        int cnt;
        boolean crash;

        Position(int x, int y, int cnt, boolean crash) {
            this.x = x;
            this.y = y;
            this.crash = crash;
            this.cnt = cnt;
        }
    }

    static boolean checkRange(int x, int y) {
        if (x >= N || x < 0) return false;
        if (y >= M || y < 0) return false;

        return true;
    }
}
